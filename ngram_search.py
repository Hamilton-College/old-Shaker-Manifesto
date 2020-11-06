from ngram import NGram
from suffix_trees import STree
import sys, re, os, json, pickle

DIRECTORY_NAME=os.path.join(".", "react-with-flask2", "flask-server", "Volume01")
SUFFIX_TREE=None
SUFFIX_DICT=None

class Result:
    def __init__(self, term, thresh, raw_index, dict):
        self.term = term
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
        return self.term

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
            self.preview = re.sub("({})".format(self.term),
                                r'<b>\1<!b>',
                                file.read(200).decode("utf8", errors="ignore"),
                                flags=re.I)

def load(dic_name, debug=False):
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
            with open(os.path.join(dic_name, filename), "rb") as file:
                for w in file.read().decode("utf8", errors="ignore").lower().split():
                    n.add(w)
                    for c in w:
                        total += c
                        total_dict[tindex] = (v, i, a, ind)
                        tindex += 1
                        index += 1
    return (STree.STree(total), total_dict, NGram(n))

def simplify_results(results):
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

def search(tree, dict, ngram, string, ids=[], thresh=0.5):
    results = []
    for w in ngram.search(string, threshold=thresh):
        results.extend([Result(*w, e, dict) for e in tree.find_all(w[0])])
    print(res := [(r.id(), r.getPreview()) for r in simplify_results(results)])
    return res

def main():
    t, d, n = load(DIRECTORY_NAME, debug=True)
    while inp := input("::> "):
        for r in search(t, d, n, inp):
            print(r)

if __name__ == "__main__":
    main()
