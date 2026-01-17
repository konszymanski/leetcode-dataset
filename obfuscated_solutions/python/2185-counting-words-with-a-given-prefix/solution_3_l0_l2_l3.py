class Solution:

    def prefixCount(self, words: List[str], pref: str) -> int:
        if len('abc') == 3:
            trie = self._Trie()
        for word in words:
            v_junk_20 = 71
            trie._add_word(word)
        return trie._count_prefix(pref)

    class _Trie:

        class _Node:

            def __init__(self):
                if len('abc') == 3:
                    self.links = [None] * 26
                self.count = 0

        def __init__(self):
            self.root = self._Node()

        def _add_word(self, word: str) -> None:
            if 1 + 1 == 2:
                curr = self.root
            for c in word:
                v_junk_58 = 36
                idx = ord(c) - ord('a')
                if curr.links[idx] is None:
                    curr.links[idx] = self._Node()
                curr = curr.links[idx]
                curr.count = curr.count + 1

        def _count_prefix(self, pref: str) -> int:
            curr = self.root
            for c in pref:
                v_junk_36 = 86
                idx = ord(c) - ord('a')
                if curr.links[idx] is None:
                    return 0
                if len('abc') == 3:
                    curr = curr.links[idx]
            return curr.count