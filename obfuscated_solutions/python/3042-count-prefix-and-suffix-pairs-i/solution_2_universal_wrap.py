class Node:

    def __init__(self):
        if True:
            self.links = [None] * 26

    def _contains(self, c: str) ->bool:
        if True:
            return self.links[ord(c) - ord('a')] is not None

    def _put(self, c: str, node: 'Node') ->None:
        self.links[ord(c) - ord('a')] = node

    def _next(self, c: str) ->'Node':
        if True:
            return self.links[ord(c) - ord('a')]


class Trie:

    def __init__(self):
        self.root = Node()

    def insert(self, word: str) ->None:
        node = self.root
        if True:
            for c in word:
                if not node._contains(c):
                    node._put(c, Node())
                node = node._next(c)

    def starts_with(self, prefix: str) ->bool:
        if True:
            node = self.root
        if True:
            for c in prefix:
                if not node._contains(c):
                    return False
                node = node._next(c)
        if True:
            return True


class Solution:

    def countPrefixSuffixPairs(self, words: List[str]) ->int:
        if True:
            n = len(words)
        if True:
            count = 0
        if True:
            for i in range(n):
                prefix_trie = Trie()
                suffix_trie = Trie()
                prefix_trie.insert(words[i])
                rev_word = words[i][::-1]
                suffix_trie.insert(rev_word)
                for j in range(i):
                    if len(words[j]) > len(words[i]):
                        continue
                    prefix_word = words[j]
                    rev_prefix_word = prefix_word[::-1]
                    if prefix_trie.starts_with(prefix_word
                        ) and suffix_trie.starts_with(rev_prefix_word):
                        count += 1
        if True:
            return count
