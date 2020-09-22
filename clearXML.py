import sys, os

def cleanXML(filename, results_dir=""):
    origf = open(filename)
    cleanf = open(results_dir + filename[filename.rindex('\\') + 1:len(filename) - 3] + "txt", "w+")
    tagf = open(results_dir + filename[filename.rindex('\\') + 1:len(filename) - 3] + "diff", "w+")

    loc = 0

    c = origf.read(1)
    tag = 0
    while c:
        if c == "<":
            tag += 1
            tagf.write(c)
            if (tag == 1): cleanf.write(' ')
        elif c == '>':
            tag -= 1
            tagf.write(c)
        elif tag == 0:
            cleanf.write(c)
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
    cleanf.close()
    tagf.close()

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

def main():
    if sys.argv[1] == "-d" and len(sys.argv) == 4:
        print("Cleaning directory: " + sys.argv[2])
        for filename in os.listdir(sys.argv[2]):
            if filename.endswith(".xml"):
                print("Cleaning file: " + filename)
                cleanXML(str(os.path.join(sys.argv[2], filename)), sys.argv[3])
    elif len(sys.argv) == 2:
        filename = sys.argv[1]
        print("Cleaning file: " + filename)
        cleanXML(filename)
    elif len(sys.argv) == 3 and sys.argv[1] == '-c':
        s = set()
        for filename in os.listdir(sys.argv[2]):
            if filename.endswith(".txt"):
                print("Processing: " + filename)
                create_dict(s, str(os.path.join(sys.argv[2], filename)))
        # print(*list(s), sep='\n')

if __name__ == "__main__":
    main()
