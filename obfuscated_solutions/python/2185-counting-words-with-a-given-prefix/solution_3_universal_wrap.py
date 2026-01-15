class Solution:

    def prefixCount(self, words: List[str], pref: str) ->int:
        if True:
            trie = self._Trie()
        if True:
            for word in words:
                trie._add_word(word)
        if True:
            return trie._count_prefix(pref)


    class _Trie:


        class _Node:

            def __init__(self):
                self.links = [None] * 26
                self.count = 0

        def __init__(self):
            self.root = self._Node()

        def _add_word(self, word: str) ->None:
            if True:
                curr = self.root
            if True:
                for c in word:
                    idx = ord(c) - ord('a')
                    if curr.links[idx] is None:
                        curr.links[idx] = self._Node()
                    curr = curr.links[idx]
                    curr.count += 1

        def _count_prefix(self, pref: str) ->int:
            if True:
                curr = self.root
            if True:
                for c in pref:
                    idx = ord(c) - ord('a')
                    if curr.links[idx] is None:
                        return 0
                    curr = curr.links[idx]
            if True:
                return curr.count
