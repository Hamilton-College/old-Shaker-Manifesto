from ngram import NGram
from suffix_trees import STree
import sys, re, os, json, pickle, time

DIRECTORY_NAME=os.path.join(".", "react-with-flask2", "flask-server", "Volume01")
PAGE_LIMIT=15

class Result:
    def __init__(self, terms, thresh, raw_index, dict):
        print(terms)
        self.terms = terms
        self.thresh = thresh
        self.raw_index = raw_index
        self.vol = -1
        self.issue = -1
        self.article = -1
        self.index = 0
        self.preview = None
        self._loc = DIRECTORY_NAME
        self.occur = 1
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

    def getOccur(self):
        return self.occur

    def _processRaw(self, dict):
        self.vol, self.issue, self.article, self.index = dict[self.raw_index]

    def filename(self):
        assert(self.vol != -1)
        assert(self.issue != -1)
        assert(self.article != -1)
        return os.path.join(DIRECTORY_NAME,
            "{:02d}{:02d}{:03d}.txt".format(self.vol, self.issue, self.article))

    def id(self):
        return self.vol * 100000 + self.issue * 1000 + self.article

    def getPreview(self):
        if self.preview is None:
            self._set_preview()
        return self.preview

    def _set_preview(self):
        start = self.index - 100 if self.index - 100 > 0 else 0
        with open(self.filename(), "rb") as file:
            file.seek(start)
            self.preview = re.sub("({})".format("|".join(self.terms)),
                                r'<b>\1<!b>',
                                file.read(200).decode("utf8", errors="ignore"),
                                flags=re.I)

class SM_Search:
    def __init__(self):
        self._tree = None
        self._index_dict = None
        self._ngram = None
        self._remain = None
        self._remain_len = 0
        self._load(DIRECTORY_NAME)

    def _load(self, dic_name, debug=False):
        total = ""
        tindex = 0
        total_dict = {}
        n = set()
        v, i, a, ind = (0, 0, 0, 0)
        r = re.compile("(\d\d)(\d\d)(\d\d\d).txt")
        for filename in sorted(os.listdir(dic_name)):
            index = 0
            if filename.endswith(".txt"):
                if debug:
                    print("Processing {}".format(filename))
                v, i, a = map(int, r.match(filename).groups())
                w = ''
                with open(os.path.join(dic_name, filename), "rb") as file:
                    for c in file.read().decode("utf8", errors="ignore").lower():
                        if c in [' ', '\t', '\n', '\r']:
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
                        total_dict[tindex] = (v, i, a, ind)
                        tindex += 1
                        index += 1


        self._tree = STree.STree(total)
        self._index_dict = total_dict
        self._ngram = NGram(n)

    def page_num(self):
        return self._remain_len // PAGE_LIMIT + 1

    def _simplify_results(self, results):
        results.sort(key=Result.getRawIndex)
        simplified = [results[0]]
        for i in range(len(results)):
            if (s:= simplified[-1]).id() == (r := results[i]).id():
                if s.getTerm() == r.getTerm():
                    s.occur += 1
                elif s.getThresh() < r.getThresh(): #r is closer to original term
                    simplified.pop()
                    simplified.append(r)
            else: #no simplification
                simplified.append(results[i])
        simplified.sort(key=Result.getThresh)
        return simplified

    def _generate_results(self):
        if self._remain:
            r = [[r.id(), r.getPreview()] for r in self._remain[:PAGE_LIMIT]]
            self._remain = self._remain[PAGE_LIMIT:]
            return r
        return []

    def _set_results(self, string, ids=[], thresh=0.5):
        results = []
        for w in self._ngram.search(string, threshold=thresh):
            results.extend([Result(*w, e, self._index_dict) for e in self._tree.find_all(w[0])])
        if results:
            results = self._simplify_results(results)
            self._remain = filter((lambda r : r.id() in ids), results) if ids else results

#pure literal search broken
#occasional failure to properly retrieve preview
#possible failure to properly find intersections for fuzzy search by word
#investigate higher thresholding to reduce run time

    def search(self, string, ids=[], thresh=0.5):
        string = string.strip().lower()
        if string:
            ids = set(ids)
            idict = dict(zip(sorted(list(ids)), [-1]*len(ids)))
            #literal search for quoted search terms
            for quote in (exact := re.findall("\".*\"", string)):
                s = set()
                print(quote[1:-1])
                for raw in self._tree.find_all(quote[1:-1]):
                    s.add(id := int("{:02d}{:02d}{:03d}".format(*(self._index_dict[raw][:3]))))
                    idict[id] = min([raw, idict.get(id, float('inf'))])
                if ids:
                    ids.intersection_update(s)
                else:
                    ids = s

            #list of fuzzy search terms
            if not (words := re.sub("\".*\"", "", string)):
                # print("pure literal case")
                # print(ids)
                self._remain = [Result(exact, 1, idict[i], self._index_dict) for i in ids]
                self._remain_len = len(self._remain)
                # print(self._remain)
                return self._generate_results()#results for pure literal search
            word = (words := words.split())[0]
            results = []
            for w in self._ngram.search(word, threshold=thresh):
                results.extend([Result([w[0]], w[1], e, self._index_dict) for e in self._tree.find_all(w[0])])
            if not results:
                return []
            results = self._simplify_results(results)
            self._remain = list(filter((lambda r : r.id() in ids), results)) if ids else results
            self._remain_len = len(self._remain)
            rdict = dict(zip(list(map(Result.id, self._remain)), self._remain))
            # print(rdict)
            for word in words[1:]:
                if not self._remain:
                    return []
                for w in self._ngram.search(word, threshold=thresh):
                    r = [(int("{:02d}{:02d}{:03d}".format(*((i := self._index_dict[e])[:3]))), i[3]) for e in self._tree.find_all(w[0])]
                    d = {}
                    for id, ind in r:
                        if (e := rdict.get(id)):
                            d[id] = e
                            e.terms += [w[0]]
                            e.index = max([e.index, ind])
                            e.thresh *= w[1]
                rdict = d
            if rdict:
                self._remain = list(rdict.values())
            self._remain.sort(key=Result.getThresh)
            self._remain_len = len(self._remain)

        return self._generate_results()

def main():
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
