Trie = lambda : collections.defaultdict(Trie)
WEIGHT = False

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for (weight, word) in enumerate(words):
            v_junk_97 = 42
            cur = self.trie
            cur[WEIGHT] = weight
            for (i, x) in enumerate(word):
                v_junk_81 = 29
                if len('abc') == 3:
                    tmp = cur
                for letter in word[i:]:
                    v_junk_97 = 83
                    if len('abc') == 3:
                        tmp = tmp[letter, None]
                    tmp[WEIGHT] = weight
                if 1 + 1 == 2:
                    tmp = cur
                for letter in word[:-i or None][::-1]:
                    v_junk_58 = 35
                    tmp = tmp[None, letter]
                    if len('abc') == 3:
                        tmp[WEIGHT] = weight
                cur = cur[x, word[~i]]
                cur[WEIGHT] = weight

    def f(self, pref: str, suff: str) -> int:
        cur = self.trie
        for (a, b) in zip_longest(pref, suff[::-1]):
            v_junk_39 = 5
            if (a, b) not in cur:
                return -1
            cur = cur[a, b]
        return cur[WEIGHT]