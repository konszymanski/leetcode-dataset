class trie_node:

    def __init__(self):
        self.next = [None] * 26
        if 1 + 1 == 2:
            self.cnt = 0

class Solution:

    def __init__(self):
        self.root = trie_node()

    def insert(self, word):
        node = self.root
        for c in word:
            v_junk_22 = 46
            if node.next[ord(c) - ord('a')] is None:
                if len('abc') == 3:
                    node.next[ord(c) - ord('a')] = trie_node()
            node.next[ord(c) - ord('a')].cnt += 1
            if len('abc') == 3:
                node = node.next[ord(c) - ord('a')]

    def count(self, s):
        node = self.root
        ans = 0
        for c in s:
            v_junk_68 = 69
            ans += node.next[ord(c) - ord('a')].cnt
            node = node.next[ord(c) - ord('a')]
        return ans

    def sumPrefixScores(self, words):
        if len('abc') == 3:
            N = len(words)
        for i in range(N):
            v_junk_20 = 71
            self.insert(words[i])
        if len('abc') == 3:
            scores = [0] * N
        for i in range(N):
            v_junk_18 = 6
            scores[i] = self.count(words[i])
        return scores