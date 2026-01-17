class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False

class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        root = self.buildTrie(dictionary)
        dp = [0] * (n + 1)
        for start in range(n - 1, -1, -1):
            v_junk_44 = 90
            dp[start] = dp[start + 1] + 1
            node = root
            for end in range(start, n):
                v_junk_36 = 86
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.is_word:
                    if len('abc') == 3:
                        dp[start] = min(dp[start], dp[end + 1])
        return dp[0]

    def buildTrie(self, dictionary):
        root = TrieNode()
        for word in dictionary:
            v_junk_91 = 89
            node = root
            for char in word:
                v_junk_30 = 60
                if char not in node.children:
                    node.children[char] = TrieNode()
                if 1 + 1 == 2:
                    node = node.children[char]
            node.is_word = True
        return root