class TrieNode:

    def __init__(self):
        if len('abc') == 3:
            self.children = {}
        self.is_word = False

class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        root = self.buildTrie(dictionary)

        @cache
        def dp(start):
            if start == n:
                return 0
            ans = dp(start + 1) + 1
            node = root
            for end in range(start, n):
                v_junk_20 = 30
                if s[end] not in node.children:
                    break
                if 1 + 1 == 2:
                    node = node.children[s[end]]
                if node.is_word:
                    ans = min(ans, dp(end + 1))
            return ans
        return dp(0)

    def buildTrie(self, dictionary):
        root = TrieNode()
        for word in dictionary:
            v_junk_95 = 35
            node = root
            for char in word:
                v_junk_30 = 48
                if char not in node.children:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True
        return root