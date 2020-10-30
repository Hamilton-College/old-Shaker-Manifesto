import sys, os, re
import xml.etree.ElementTree as ET
from functools import reduce

SAVE_LOC = "shaker_dictionary.txt"

def get_xml_names(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    names = []
    xml_traverse(root, names)
    return names

def xml_traverse(root, names):
    for elem in root:
        if elem.attrib.get("TEIform") == "persName":
            names.append(elem.attrib.get("reg"))
        xml_traverse(elem, names)

def create_dict(s, filename):
    f = open(filename, encoding="utf8")
    for line in f:
        for word in line.split():
            s.add(word.lower())

    f.close()

    w = open(SAVE_LOC, "a", encoding="utf8")
    for word in list(s):
        w.write(word)
        w.write("\n")
    w.close()

def clean_text(filename):
    l = []
    with open(filename, encoding="utf8") as f:
        for line in f.readlines():
            word = ""
            for c in line:
                if ord('A') <= ord(c) and ord(c) <= ord('Z') or\
                        ord('a') <= ord(c) and ord(c) <= ord('z'):
                    word += c
                elif word and word[-1] != ' ' and c in [' ', '\t', '\n', '\r', '.', ',', '-', '\"', "?"]:
                    word += ' '
            for w in word.split():
                l.append(w.strip())
    with open(SAVE_LOC, "w+", encoding="utf8") as output:
        for l in sorted(list(set(l))):
            output.write(l)
            output.write('\n')

def main():
    if len(sys.argv) == 2:
        open("temp.txt", "w+").close() #cleans contents of existing dictionary
        s = set()
        for filename in os.listdir(sys.argv[1]):
            if filename.endswith(".txt"):
                print("Processing: " + filename)
                create_dict(s, str(os.path.join(sys.argv[1], filename)))
        clean_text(SAVE_LOC)
        os.remove("temp.txt")
    elif len(sys.argv) == 3 and sys.argv[1] == '-n':
        n = get_xml_names(sys.argv[2])
        print(n)
    elif len(sys.argv) == 3 and sys.argv[1] == "-d":
        names = []
        for filename in os.listdir(sys.argv[2]):
            if filename.endswith(".xml"):
                # print("Gathering names from: " + filename)
                names.extend(get_xml_names(str(os.path.join(sys.argv[2], filename))))
        l = []
        for ns in list(set(names)):
            ns = str(ns)
            if ';' in ns:
                for n in ns.split(';'):
                    l.append(" ".join(n.split()))
            elif "and" in ns:
                for n in ns.split('and'):
                    l.append(" ".join(n.split()))
            else:
                l.append(" ".join(ns.split()))
        l.remove("Editor")
        print(*[str(n).strip() for n in l], sep='\n')

    else:
        print("Command Line args are invalid.")

if __name__ == "__main__":
    main()
