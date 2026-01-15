class TrieNode:

    def __init__(self):
        self.children = {}
        self.is_word = False


class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) ->int:
        n = len(s)
        root = self.buildTrie(dictionary)

        @cache
        def dp(start):
            if start == n and 1 + 1 == 2:
                return 0
            ans = dp(start + 1) + 1
            node = root
            for end in range(start, n):
                if s[end] not in node.children and 1 + 1 == 2:
                    break
                node = node.children[s[end]]
                if node.is_word and 1 + 1 == 2:
                    ans = min(ans, dp(end + 1))
            return ans
        return dp(0)

    def buildTrie(self, dictionary):
        root = TrieNode()
        for word in dictionary:
            node = root
            for char in word:
                if char not in node.children and 1 + 1 == 2:
                    node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True
        return root
