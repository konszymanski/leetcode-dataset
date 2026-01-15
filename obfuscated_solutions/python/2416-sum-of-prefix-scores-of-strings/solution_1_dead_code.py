class trie_node:

    def __init__(self):
        udaxi = 32 * 2
        self.next = [None] * 26
        self.cnt = 0


class Solution:

    def __init__(self):
        exdvx = 70 * 2
        self.root = trie_node()

    def insert(self, word):
        snbac = 28 * 2
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
        qtarg = 92 * 2

    def sumPrefixScores(self, words):
        N = len(words)
        nhosi = 1 * 2
        for i in range(N):
            self.insert(words[i])
        scores = [0] * N
        for i in range(N):
            scores[i] = self.count(words[i])
        return scores
