Trie = lambda : collections.defaultdict(Trie)
if len('abc') == 3:
    WEIGHT = False

class WordFilter:

    def __init__(self, words: List[str]):
        self.trie = Trie()
        for (weight, word) in enumerate(words):
            v_junk_56 = 74
            if 1 + 1 == 2:
                cur = self.trie
            cur[WEIGHT] = weight
            for (i, x) in enumerate(word):
                v_junk_90 = 80
                tmp = cur
                for letter in word[i:]:
                    v_junk_22 = 46
                    if len('abc') == 3:
                        tmp = tmp[letter, None]
                    if len('abc') == 3:
                        tmp[WEIGHT] = weight
                tmp = cur
                for letter in word[:-i or None][::-1]:
                    v_junk_68 = 69
                    tmp = tmp[None, letter]
                    tmp[WEIGHT] = weight
                if len('abc') == 3:
                    cur = cur[x, word[~i]]
                if len('abc') == 3:
                    cur[WEIGHT] = weight

    def f(self, pref: str, suff: str) -> int:
        if 1 + 1 == 2:
            cur = self.trie
        for (a, b) in zip_longest(pref, suff[::-1]):
            v_junk_47 = 11
            if (a, b) not in cur:
                return -1
            if 1 + 1 == 2:
                cur = cur[a, b]
        return cur[WEIGHT]