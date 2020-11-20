from ngram import NGram
from suffix_trees import STree
import sys, re, os, json, time

DIRECTORY_NAME=os.path.join(".", "flask-server", "Volume01")
PAGE_LIMIT=15 #number of results per page

class Result:
    def __init__(self, terms=[], thresh=0, raw_index=0, dict={}, load=False):
        if load:
            self.__dict__.update(dict)
            return
        self.terms = terms          #list of search terms contained in result
        self.thresh = thresh        #combined search threshold via ngram similarity
        self.raw_index = raw_index  #raw index from entire search directory
        self.vol = -1
        self.issue = -1
        self.article = -1
        self.index = 0              #index within specified article
        self.preview = None
        if dict:
            self._processRaw(dict)

    def getTerm(self):
        return self.terms

    def getThresh(self):
        return self.thresh

    def getRawIndex(self):
        return self.raw_index

    def getVol(self):
        return self.vol

    def getIssue(self):
        return self.issue

    def getArticle(self):
        return self.article

    def _processRaw(self, dict):
        """sets volume, issue, article, and index fields based on the passed
        dictionary and raw_index"""
        self.vol, self.issue, self.article, self.index = dict[self.raw_index]

    def filename(self):
        """only callable after _processRaw"""
        assert(self.vol != -1)
        assert(self.issue != -1)
        assert(self.article != -1)
        return os.path.join(DIRECTORY_NAME, "{:07d}.txt".format(self.id()))

    def id(self):
        """only callable after _processRaw"""
        return self.vol * 100000 + self.issue * 1000 + self.article

    def getPreview(self):
        """sets preview field if no preview is stored and returns the stored
        preview in all cases"""
        if self.preview is None:
            self._set_preview()
        return self.preview

    def _set_preview(self):
        """sets the preview field and inserts bolding for frontend display"""
        start = max([self.index - 100, 0])
        with open(self.filename(), "rb") as file:
            file.seek(start)
            self.preview = re.sub("({})".format("|".join(self.terms)),
                                r'<b>\1<!b>',
                                file.read(200).decode("utf8", errors="ignore"),
                                flags=re.I)

class SM_Search:
    def __init__(self):
        self._tree = None           #searchable suffix tree
        self._index_dict = None     #dictionary from raw_index to volume, issue, article and index
        self._ngram = None          #ngram object for entire search range
        self._remain = None         #current search result
        self._load(DIRECTORY_NAME)


    def store_results(self):
        return json.dumps([vars(r) for r in self._remain])

    def load_results(self, results):
        self._remain = [Result(dict=d, load=True) for d in json.loads(results)]

    def _load(self, dic_name, debug=False):
        """reads the .txt files from the given directory and builds the ngram
        and suffix tree data structures necessary for the search, as well as the
        conversion dictionary"""
        total = ""
        tindex = 0
        total_dict = {}
        n = set()
        v, i, a = (0, 0, 0)
        r = re.compile("(\d\d)(\d\d)(\d\d\d).txt")
        for filename in sorted(os.listdir(dic_name)):
            index = 0
            if filename.endswith(".txt"):
                if debug:
                    print("Processing {}".format(filename))
                v, i, a = map(int, r.match(filename).groups())
                w = ''
                with open(os.path.join(dic_name, filename), "rb") as file:
                    for c in file.read().decode("utf8", errors="replace").lower():
                        if c in [' ', '\t', '\n', '\r', '\ufffd']:
                            if total[-1] == ' ':
                                index += 1
                                continue
                            else:
                                total += ' '
                                n.add(w)
                                w = ''
                        else:
                            total += c
                            w += c
                        total_dict[tindex] = (v, i, a, index)
                        tindex += 1
                        index += 1


        self._tree = STree.STree(total)
        self._index_dict = total_dict
        self._ngram = NGram(n)

    def page_num(self):
        """returns the number of pages of results currently stored in _remain"""
        return (l := len(self._remain)) // PAGE_LIMIT + bool(l % PAGE_LIMIT)

    def _simplify_results(self, results):
        """simplifies the results of a single fuzzy search"""
        results.sort(key=Result.getRawIndex)
        simplified = [results[0]]
        for i in range(len(results)):
            if (s:= simplified[-1]).id() == (r := results[i]).id():
                if s.getThresh() < r.getThresh(): #r is closer to original term
                    simplified.pop()
                    simplified.append(r)
            else: #no simplification
                simplified.append(results[i])
        simplified.sort(key=Result.getThresh)
        return simplified

    def _generate_results(self, pg_num = 0):
        """generate and return a page worth of results"""
        if self._remain and pg_num <= self.page_num():
            return [[r.id(), r.getPreview()] for r in self._remain[pg_num*PAGE_LIMIT: (pg_num + 1)*PAGE_LIMIT]]
        return []

    def search(self, string, ids=[], thresh=0.5):
        """conduct a fuzzy search and/or literal search (denoted by a quoted
        string) constrained to the given list of ids (if applicable) and returns
        the first page of results. If no search term is passed, returns the
        first page of results of the stored search"""
        # print(string)
        string = string.strip().lower()
        c = re.compile("\".*?\"")
        if string:
            ids = set(ids)
            idict = dict(zip(sorted(list(ids)), [-1]*len(ids)))
            #literal search for quoted search terms
            for quote in (exact := [s[1:-1] for s in c.findall(string)]):
                s = set()
                # print(quote)
                for raw in self._tree.find_all(quote):
                    s.add(id := int("{:02d}{:02d}{:03d}".format(*(self._index_dict[raw][:3]))))
                    idict[id] = min([raw, idict.get(id, float('inf'))])
                if ids:
                    ids.intersection_update(s)
                else:
                    ids = s

            #list of fuzzy search terms
            if not (words := c.sub("", string).strip()):
                # print("pure literal case")
                # print(ids)
                self._remain = [Result(exact, 1, idict[i], self._index_dict) for i in ids]
                # print(self._remain)
                return self.generate_results()#results for pure literal search
            # print(words)
            word = (words := words.split())[0]
            results = []
            for w in self._ngram.search(word, threshold=thresh):
                results.extend([Result([w[0]], w[1], e, self._index_dict) for e in self._tree.find_all(w[0])])
            if not results:
                return []
            results = self._simplify_results(results)
            self._remain = list(filter((lambda r : r.id() in ids), results)) if ids else results
            rdict = dict(zip(list(map(Result.id, self._remain)), self._remain))
            # print(rdict)
            for word in words[1:]:
                # print("additional fuzzy")
                if not self._remain:
                    return []
                for w in self._ngram.search(word, threshold=thresh):
                    r = [(int("{:02d}{:02d}{:03d}".format(*((i := self._index_dict[e])[:3]))), i[3]) for e in self._tree.find_all(w[0])]
                    d = {}
                    for id, ind in r:
                        if (e := rdict.get(id)):
                            d[id] = e
                            e.terms += [w[0]]
                            e.index = min([e.index, ind])
                            e.thresh *= w[1]
                rdict = d
            if rdict:
                self._remain = list(rdict.values())
            self._remain.sort(key=Result.getThresh)

        return self._generate_results()

def main():
    """testing command line interface"""
    tic = time.perf_counter()
    s = SM_Search()
    print(time.perf_counter() - tic)
    while (inp := input("::> ")) != "exit":
        tic = time.perf_counter()
        result = s.search(inp)
        for r in result:
            print(r)
        print(time.perf_counter() - tic)

if __name__ == "__main__":
    main()
