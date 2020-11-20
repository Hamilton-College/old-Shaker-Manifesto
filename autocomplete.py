from fast_autocomplete import AutoComplete

class SM_Autocomplete:

    def __init__(self):
        with open("shaker_dictionary.txt", "r", encoding="utf8") as file:
            words = file.readlines()
        words = dict(zip(words, [dict()] * len(words)))
        self.autocomplete = AutoComplete(words=words)

        with open("authors.txt", "r", encoding="utf8") as f:
            names = file.readlines()
        names = dict(zip(names, [dict()] * len(names)))
        self.authors = AutoComplete(words=names)


    def general(self, s):
        return sorted(AUTOCOMPLETE.search(word=s, max_cost=3, size=10))

    def author(self, s):
        return sorted(AUTHORS.search(word=s, max_cost=3, size=10))

def main():
    ac = SM_Autocomplete
    while (s := input("::>")) != "exit":
        print(*ac.general(s), sep='\n')


if __name__ == "__main__":
    main()
