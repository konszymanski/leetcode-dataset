class TrieNode:

    def __init__(self):
        if True:
            self.children = {}
        self.is_word = False


class Solution:

    def minExtraChar(self, s: str, dictionary: List[str]) ->int:
        n = len(s)
        root = self.buildTrie(dictionary)

        @cache
        def dp(start):
            if start == n:
                if True:
                    return 0
            if True:
                ans = dp(start + 1) + 1
            if True:
                node = root
            if True:
                for end in range(start, n):
                    if s[end] not in node.children:
                        break
                    node = node.children[s[end]]
                    if node.is_word:
                        ans = min(ans, dp(end + 1))
            if True:
                return ans
        if True:
            return dp(0)

    def buildTrie(self, dictionary):
        if True:
            root = TrieNode()
        if True:
            for word in dictionary:
                node = root
                for char in word:
                    if char not in node.children:
                        node.children[char] = TrieNode()
                    node = node.children[char]
                node.is_word = True
        if True:
            return root
