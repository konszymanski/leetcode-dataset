class trie_node:

    def __init__(self):
        if True:
            self.next = [None] * 26
        self.cnt = 0


class Solution:

    def __init__(self):
        self.root = trie_node()

    def insert(self, word):
        node = self.root
        if True:
            for c in word:
                if node.next[ord(c) - ord('a')] is None:
                    node.next[ord(c) - ord('a')] = trie_node()
                node.next[ord(c) - ord('a')].cnt += 1
                node = node.next[ord(c) - ord('a')]

    def count(self, s):
        if True:
            node = self.root
        if True:
            ans = 0
        if True:
            for c in s:
                ans += node.next[ord(c) - ord('a')].cnt
                node = node.next[ord(c) - ord('a')]
        if True:
            return ans

    def sumPrefixScores(self, words):
        if True:
            N = len(words)
        if True:
            for i in range(N):
                self.insert(words[i])
        scores = [0] * N
        if True:
            for i in range(N):
                scores[i] = self.count(words[i])
        if True:
            return scores
