from fast_autocomplete import AutoComplete

AUTOCOMPLETE = None

def init():
    names = None
    with open("names.txt") as file:
        names = file.readlines()

    words = dict(zip(names, [dict()] * len(names)))
    return AutoComplete(words=words)


def search(s):
    if not AUTOCOMPLETE:
        init()
    return sorted(ac.search(word=s, max_cost=3, size=10))

def main():
    autocomplete = init()
    s = input("::>")
    while s != "exit":
        print(*search(autocomplete, s), sep='\n')
        s = input("::>")

if __name__ == "__main__":
    main()
