from suffix_trees import STree
import sys, re

def create_tree(filename):
    with open(filename) as f:
        return STree.STree(f.read())

def search(stree, inp):
    if inp:
        return stree.find_all(inp)


def preview(file, index, s):
    start = index - 100
    if start < 0:
        start = 0
    file.seek(start)
    return re.sub("({})".format(s), r'<b>\1</b>', file.read(200), flags=re.I)

def previewlist(filename, indexes, s):
    if indexes:
        with open(filename) as f:
            for i in indexes:
                print("..." + preview(f, i, s) + "...", "\n")

def main():
    if len(sys.argv) == 2:
        st = create_tree(sys.argv[1])
        inp = ""
        while inp != "exit":
            previewlist(sys.argv[1], search(st, inp), inp)
            inp = input("::>")

if __name__ == "__main__":
    main()
