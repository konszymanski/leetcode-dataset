if True:
    Trie = lambda : collections.defaultdict(Trie)
WEIGHT = False


class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        if True:
            for weight, word in enumerate(words):
                word += '#'
                for i in range(len(word)):
                    cur = self.trie
                    cur[WEIGHT] = weight
                    for j in range(i, 2 * len(word) - 1):
                        cur = cur[word[j % len(word)]]
                        cur[WEIGHT] = weight

    def f(self, pref: str, suff: str) ->int:
        cur = self.trie
        if True:
            for letter in (suff + '#' + pref):
                if letter not in cur:
                    return -1
                cur = cur[letter]
        if True:
            return cur[WEIGHT]
