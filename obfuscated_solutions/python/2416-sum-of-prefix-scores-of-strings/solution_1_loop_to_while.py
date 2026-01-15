class trie_node:

    def __init__(self):
        self.next = [None] * 26
        self.cnt = 0


class Solution:

    def __init__(self):
        self.root = trie_node()

    def insert(self, word):
        node = self.root
        for c in word:
            if node.next[ord(c) - ord('a')] is None:
                node.next[ord(c) - ord('a')] = trie_node()
            node.next[ord(c) - ord('a')].cnt += 1
            node = node.next[ord(c) - ord('a')]

    def count(self, s):
        node = self.root
        ans = 0
        for c in s:
            ans += node.next[ord(c) - ord('a')].cnt
            node = node.next[ord(c) - ord('a')]
        return ans

    def sumPrefixScores(self, words):
        N = len(words)
        i = 0
        while i < N:
            self.insert(words[i])
            i += 1
        scores = [0] * N
        i = 0
        while i < N:
            scores[i] = self.count(words[i])
            i += 1
        return scores
