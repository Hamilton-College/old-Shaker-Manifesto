from fast_autocomplete import AutoComplete
from pkg_resources import resource_stream as stream

class SM_Autocomplete:

    def __init__(self):
        with open("shaker_dictionary.txt", "r", encoding="utf8") as f:
        #with stream(__name__, 'shaker_dictionary.txt') as f:
            words = f.readlines()
        words = dict(zip(words, [dict()] * len(words)))
        self.autocomplete = AutoComplete(words=words)

        with open("authors.txt", "r", encoding="utf8") as f:
        #with stream(__name__, 'authors.txt') as f:
            names = f.readlines()
        names = dict(zip(names, [dict()] * len(names)))
        self.authors = AutoComplete(words=names)

    def general(self, s):
        return sorted(self.autocomplete.search(word=s, max_cost=3, size=10))

    def author(self, s):
        return sorted(self.authors.search(word=s, max_cost=3, size=10))

def main():
    ac = SM_Autocomplete()
    while (s := input("::>")) != "exit":
        print(s)
        print(*(ac.general(s)), sep='\n')


if __name__ == "__main__":
    main()
