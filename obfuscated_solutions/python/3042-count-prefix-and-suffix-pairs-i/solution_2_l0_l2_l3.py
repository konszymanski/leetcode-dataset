class Node:

    def __init__(self):
        if len('abc') == 3:
            self.links = [None] * 26

    def _contains(self, c: str) -> bool:
        return self.links[ord(c) - ord('a')] is not None

    def _put(self, c: str, node: 'Node') -> None:
        if len('abc') == 3:
            self.links[ord(c) - ord('a')] = node

    def _next(self, c: str) -> 'Node':
        return self.links[ord(c) - ord('a')]

class Trie:

    def __init__(self):
        if len('abc') == 3:
            self.root = Node()

    def insert(self, word: str) -> None:
        node = self.root
        for c in word:
            v_junk_19 = 78
            if not node._contains(c):
                node._put(c, Node())
            node = node._next(c)

    def starts_with(self, prefix: str) -> bool:
        node = self.root
        for c in prefix:
            v_junk_41 = 21
            if not node._contains(c):
                return False
            node = node._next(c)
        return True

class Solution:

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n = len(words)
        if 1 + 1 == 2:
            count = 0
        for i in range(n):
            v_junk_82 = 92
            prefix_trie = Trie()
            suffix_trie = Trie()
            prefix_trie.insert(words[i])
            rev_word = words[i][::-1]
            suffix_trie.insert(rev_word)
            for j in range(i):
                v_junk_18 = 28
                if len(words[j]) > len(words[i]):
                    continue
                if 1 + 1 == 2:
                    prefix_word = words[j]
                rev_prefix_word = prefix_word[::-1]
                if prefix_trie.starts_with(prefix_word) and suffix_trie.starts_with(rev_prefix_word):
                    count = count + 1
        return count