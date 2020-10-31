from suffix_trees import STree
from SMTree import FuzzyTree
import sys, re, os, json, pickle, time

DIRECTORY_NAME=os.path.join(".", "Volume01")
SUFFIX_TREE=None
SUFFIX_DICT=None

def create_tree(dic_name, debug=False):
        total = ""
        total_index = 0
        total_dict = {}
        (v, i, a, index) = (0, 0, 0, 0)
        r = re.compile("(\d\d)(\d\d)(\d\d\d).txt", re.ASCII)
        for filename in sorted(os.listdir(dic_name)):
            index = 0
            if filename.endswith(".txt"):
                if debug:
                    print(filename)
                (v, i, a) = map(int, r.match(str(filename)).groups())
                with open(os.path.join(dic_name, filename), 'r', encoding="utf8") as file:
                    for c in file.read():
                        if c.isascii():
                            total += c.lower()
                            total_dict[total_index] = (v, i, a, index)
                            total_index += 1
                            index += 1
        return (FuzzyTree(total.lower()), total_dict)

# INPUT: list with elements (article id, index)
# OUTPUT: list with elements (article id, index, occurances)
#           each article id is now unique
def simplify_results(results):
    results.sort()
    simplified = [[*results[0], 0]]
    for i in range(len(results)):
        if simplified[-1][0] == results[i][0]:
            simplified[-1][2] += 1
        else:
            simplified.append([*results[i], 1])
    return simplified

def articleSearch(inp, articleIDs=[]):
    print("in articleSearch")
    assert(inp)
    global SUFFIX_TREE, SUFFIX_DICT
    if not SUFFIX_TREE:
        SUFFIX_TREE, SUFFIX_DICT = create_tree(DIRECTORY_NAME)
    if results := SUFFIX_TREE.find(inp.lower()):
        l = simplify_results([(int("{:02d}{:02d}{:03d}".format(*SUFFIX_DICT[i][:3])), SUFFIX_DICT[i][3]) for i in sorted(results)])
        previews = previewlist(DIRECTORY_NAME, [ ("{:07d}.txt".format(elem[0]), elem[1]) for elem in l], inp.lower())
        return_list = [[l[i][0], previews[i], l[i][2]] for i in range(len(previews))]
        if articleIDs:
            return list(filter(lambda n: n[0] in articleIDs, return_list))
        return return_list

def preview(file, index, s):
    start = index - 100 if index - 100 > 0 else 0
    file.seek(start)
    p = str(file.read(200))
    f = FuzzyTree(p)
    r = ""
    b = False
    for i in range(len(p)):
        if i in f.find(s):
            r += "<b>"
            b = i
        if b and i > b + len(s) and p[i] == ' ':
            b = 0
            r += "<!b>"
        r += p[i]
    return r


def previewlist(dictname, locations, searchstring):
    assert(dictname)
    assert(locations)
    assert(searchstring)
    results = []
    for filename, index in locations:
        with open(os.path.join(dictname, filename), "rb") as file:
            results.append("...{}...".format(preview(file, index, searchstring)))
    return results

def main():
    if len(sys.argv) == 2:
        st, d = create_tree(sys.argv[1])
        while (inp:= input("::>")) != "exit":
            if inp:
                if results := articleSearch(inp.lower()):
                    for result in results:
                        print("{}: {}".format(*result))
                else:
                    print("No Matches Found")
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-t':
            store_test(sys.argv[2])

if __name__ == "__main__":
    main()
