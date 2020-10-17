from suffix_trees import STree
import sys, re, os, json, pickle, time

DIRECTORY_NAME=".\Volume01\\"
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
        return (STree.STree(total), total_dict)

def search(inp, articleIDs=[]):
    assert(inp)
    global SUFFIX_TREE, SUFFIX_DICT
    if not SUFFIX_TREE:
        SUFFIX_TREE, SUFFIX_DICT = create_tree(DIRECTORY_NAME)
    if results := SUFFIX_TREE.find_all(inp.lower()):
        previews = previewlist(DIRECTORY_NAME, [("{:02d}{:02d}{:03d}.txt".format(*SUFFIX_DICT[i][:3]), SUFFIX_DICT[i][3]) for i in sorted(results)], inp.lower())
        return_list = list(zip([int("{:02d}{:02d}{:03d}".format(*SUFFIX_DICT[i][:3])) for i in sorted(results)], previews))
        if articleIDs:
            return list(filter(lambda n: n[0] in articleIDs, return_list))
        return return_list



def preview(file, index, s):
    start = index - 100 if index - 100 > 0 else 0
    file.seek(start)
    return re.sub("({})".format(s), r'<b>\1</b>', str(file.read(200)), flags=re.I)

def previewlist(dictname, locations, searchstring):
    assert(dictname)
    assert(locations)
    assert(searchstring)
    results = []
    for filename, index in locations:
        with open(os.path.join(dictname, filename), "rb") as file:
            results.append("...{}...\n".format(preview(file, index, searchstring)))
    return results

def main():
    if len(sys.argv) == 2:
        st, d = create_tree(sys.argv[1])
        while (inp:= input("::>")) != "exit":
            if inp:
                if results := search(inp.lower()):
                    for result in results:
                        print("{}: {}".format(*result))
                else:
                    print("No Matches Found")
    elif len(sys.argv) == 3:
        if sys.argv[1] == '-t':
            store_test(sys.argv[2])

if __name__ == "__main__":
    main()
