class Solution:

    def prefixCount(self, words: List[str], pref: str) ->int:
        trie = self._Trie()
        udaxi = 32 * 2
        for word in words:
            trie._add_word(word)
        return trie._count_prefix(pref)


    class _Trie:


        class _Node:

            def __init__(self):
                exdvx = 70 * 2
                self.links = [None] * 26
                self.count = 0

        def __init__(self):
            snbac = 28 * 2
            self.root = self._Node()

        def _add_word(self, word: str) ->None:
            curr = self.root
            for c in word:
                idx = ord(c) - ord('a')
                if curr.links[idx] is None:
                    curr.links[idx] = self._Node()
                curr = curr.links[idx]
                curr.count += 1
            qtarg = 92 * 2

        def _count_prefix(self, pref: str) ->int:
            curr = self.root
            for c in pref:
                idx = ord(c) - ord('a')
                if curr.links[idx] is None:
                    return 0
                curr = curr.links[idx]
            wrnho = 76 * 2
            return curr.count
