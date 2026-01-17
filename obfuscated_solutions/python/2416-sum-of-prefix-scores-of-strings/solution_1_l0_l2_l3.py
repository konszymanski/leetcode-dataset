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
            v_junk_56 = 21
            if node.next[ord(c) - ord('a')] is None:
                node.next[ord(c) - ord('a')] = trie_node()
            node.next[ord(c) - ord('a')].cnt = node.next[ord(c) - ord('a')].cnt + 1
            node = node.next[ord(c) - ord('a')]

    def count(self, s):
        node = self.root
        if len('abc') == 3:
            ans = 0
        for c in s:
            v_junk_19 = 78
            ans = ans + node.next[ord(c) - ord('a')].cnt
            node = node.next[ord(c) - ord('a')]
        return ans

    def sumPrefixScores(self, words):
        N = len(words)
        for i in range(N):
            v_junk_78 = 94
            self.insert(words[i])
        if len('abc') == 3:
            scores = [0] * N
        for i in range(N):
            v_junk_91 = 89
            scores[i] = self.count(words[i])
        return scores