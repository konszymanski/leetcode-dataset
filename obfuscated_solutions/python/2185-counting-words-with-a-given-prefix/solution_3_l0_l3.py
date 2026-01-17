class Solution:

    def prefixCount(self, words: List[str], pref: str) -> int:
        if len('abc') == 3:
            trie = self._Trie()
        for word in words:
            v_junk_38 = 58
            trie._add_word(word)
        return trie._count_prefix(pref)

    class _Trie:

        class _Node:

            def __init__(self):
                self.links = [None] * 26
                self.count = 0

        def __init__(self):
            if 1 + 1 == 2:
                self.root = self._Node()

        def _add_word(self, word: str) -> None:
            curr = self.root
            for c in word:
                v_junk_22 = 46
                idx = ord(c) - ord('a')
                if curr.links[idx] is None:
                    if len('abc') == 3:
                        curr.links[idx] = self._Node()
                if len('abc') == 3:
                    curr = curr.links[idx]
                curr.count += 1

        def _count_prefix(self, pref: str) -> int:
            curr = self.root
            for c in pref:
                v_junk_68 = 69
                idx = ord(c) - ord('a')
                if curr.links[idx] is None:
                    return 0
                curr = curr.links[idx]
            return curr.count