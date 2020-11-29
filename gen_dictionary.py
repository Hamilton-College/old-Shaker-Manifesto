import sys, os, re
import xml.etree.ElementTree as ET
from functools import reduce

SAVE_LOC = "shaker_dictionary.txt"
COMMAND_LOC = "authors.txt"

def create_common(directory):
    """Finds list of words common to all txt files in directory"""
    s = set()
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            a = set()
            with open(os.path.join(directory, filename), "rb") as f:
                file = re.sub("[,'.]", "", f.read().decode("utf8", errors="ignore").lower())
            if not file:
                continue
            for w in file.split():
                a.add(w)
            if s:
                s.intersection_update(a)
            else:
                s = a

    s.discard("b")
    for w in list(s):
        if w[-1] == 's':
            s.discard(w)
            s.add(w[:-1])
    with open("common.txt", "w+") as output:
        output.write("\n".join(sorted(list(s))))

def create_names():
    """Compiles short list of names based on contents of names.csv
    Use SQL database to generate names.csv"""
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
    """Creates and filters general dicitionary based on all txt files
    in given directory"""
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
    """Command line based control interface"""
    if len(sys.argv) == 2:
        if sys.argv[1] == '-a':
            create_names()
        else:
            create_dictionary(sys.argv[1])
    elif len(sys.argv) == 3 and sys.argv[1] == '-i':
        create_common(sys.argv[2])
    else:
        print("Command Line args are invalid.")

if __name__ == "__main__":
    main()
