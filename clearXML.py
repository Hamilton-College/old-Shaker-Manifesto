import sys, os, re
import xml.etree.ElementTree as ET
from functools import reduce

def cleanXML(filename, results_dir=""):
    origf = open(filename)
    temp = open("temp.txt", "w+")
    tagf = open(results_dir + filename[filename.rindex('\\') + 1:len(filename) - 3] + "diff", "w+")

    loc = 0

    c = origf.read(1)
    tag = 0
    while c:
        if c == "<":
            tag += 1
            tagf.write(c)
            if (tag == 1): temp.write(' ')
        elif c == '>':
            tag -= 1
            tagf.write(c)
            temp.write(' ')
        elif tag == 0:
            temp.write(c)
        else:
            tagf.write(c)
        while True:
            try:
                loc = origf.tell()
                c = origf.read(1)
                break
            except UnicodeDecodeError:
                print(loc + 1)
                continue

    origf.close()
    temp.close()
    tagf.close()

    cleanf = open(results_dir + filename[filename.rindex('\\') + 1:len(filename) - 3] + "txt", "w+")
    temp = open("temp.txt", "r")

    for line in temp:
        for word in line.split():
            if word:
                cleanf.write(word)
                cleanf.write(" ")

    cleanf.close()
    temp.close()
    os.remove("temp.txt")

def create_dict(s, filename):
    f = open(filename)
    for line in f:
        for word in line.split():
            s.add(word.lower())

    f.close()

    w = open("shaker_dictionary.txt", "w+")
    for word in list(s):
        w.write(word)
        w.write("\n")
    w.close()

def get_xml_names(filename):
    tree = ET.parse(filename)
    root = tree.getroot()
    names = []
    xml_traverse(root, names)
    return names

    # dict = {}
    # xml = open(filename, "r")
    # print("Retrieving names from: " + filename)
    # r = re.compile("<persName\s*reg=\"(?P<name>[^\"]+)\"\s*TEIform=\"persName\"((/>)|(>\s*(?P<alias>[^<]+)\s*</persName>))")
    #
    # c = xml.read(1)
    # while c:
    #     if c == '<' and xml.read(8) == 'persName':
    #         tag = "<persName"
    #         print("enter loop")
    #         while r.match(tag) is None:
    #             c = xml.read(1)
    #             # if not c:
    #             #     break
    #             tag += c
    #         print(tag)
    #         m = r.match(tag)
    #         if m:
    #             print(m.groups())
    #             dict.get(m.group("name").strip(), []).append(m.group("alias"))
    #             # dict[m.group("alias").strip()] = m.group("name").strip()
    #
    #     while True:
    #         try:
    #             loc = xml.tell()
    #             c = xml.read(1)
    #             break
    #         except UnicodeDecodeError:
    #             print(loc + 1)
    #             continue
    #
    # xml.close()
    # return dict

def xml_traverse(root, names):
    for elem in root:
        if elem.attrib.get("TEIform") == "persName":
            names.append(elem.attrib.get("reg"))
        xml_traverse(elem, names)


def main():
    if sys.argv[1] == "-d" and len(sys.argv) == 4:
        print("Cleaning directory: " + sys.argv[2])
        for filename in os.listdir(sys.argv[2]):
            if filename.endswith(".xml"):
                print("Cleaning file: " + filename)
                cleanXML(str(os.path.join(sys.argv[2], filename)), sys.argv[3])
    elif len(sys.argv) == 2:
        # filename = sys.argv[1]
        # print("Cleaning file: " + filename)
        # cleanXML(filename)
        f = open(sys.argv[1])
        print(*sorted(list(set([line.strip() for line in f]))), sep='\n')
    elif len(sys.argv) == 3 and sys.argv[1] == '-c':
        s = set()
        for filename in os.listdir(sys.argv[2]):
            if filename.endswith(".txt"):
                print("Processing: " + filename)
                create_dict(s, str(os.path.join(sys.argv[2], filename)))
        # print(*list(s), sep='\n')
    elif len(sys.argv) == 3 and sys.argv[1] == '-n':
        n = get_xml_names(sys.argv[2])
        print(n)
    elif len(sys.argv) == 3 and sys.argv[1] == "-nd":
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
