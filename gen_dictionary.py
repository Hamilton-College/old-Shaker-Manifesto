import sys, os, re
import xml.etree.ElementTree as ET
from functools import reduce

SAVE_LOC = "shaker_dictionary.txt"
COMMAND_LOC = "authors.txt"

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

def create_names():
    with open("names.csv", "r") as f:
        contents = f.read()
    authors = set()
    for n in contents.split('\n'):
        authors.add(re.sub("[\"\']", "", n))
    authors.discard("")
    authors.discard("regauthor")
    with open(COMMAND_LOC, "w+", encoding="utf8") as output:
        output.write("\n".join(sorted(list(authors))))
    print(sorted(list(authors)))

def create_dictionary(directory):
    s = set()
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            print("---Processing {}---".format(filename))
            with open(os.path.join(directory, filename), "rb") as f:
                file = f.read().decode("utf8", errors="ignore")
                for w in file.split():
                    s.add(re.sub("[-.,\"?\\\\/()!#$;:%&{}=0-9'*+|~\[\]^_]", "", w).lower())

    with open("general_dictionary.txt", "r") as f:
        l = f.read().split()

    s.discard("") #remove empty string
    t = s.copy()
    for w in t:
        if len(w) < 4 or w not in l:
            s.discard(w)
        if w + "s" in s:
            s.discard(w + "s")

    with open(SAVE_LOC, "w+", encoding="utf8") as output:
        for l in sorted(list(s)):
            output.write(l + "\n")

def main():
    if len(sys.argv) == 2:
        if sys.argv[1] == '-a':
            create_names()
        else:
            create_dictionary(sys.argv[1])
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
