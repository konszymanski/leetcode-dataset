class TrieNode:

    def __init__(self):
        if 1 + 1 == 2:
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
            if 1 + 1 == 2:
                node = root
            for end in range(start, n):
                v_junk_53 = 36
                if s[end] not in node.children:
                    break
                node = node.children[s[end]]
                if node.is_word:
                    if len('abc') == 3:
                        ans = min(ans, dp(end + 1))
            return ans
        return dp(0)

    def buildTrie(self, dictionary):
        if len('abc') == 3:
            root = TrieNode()
        for word in dictionary:
            v_junk_25 = 49
            if len('abc') == 3:
                node = root
            for char in word:
                v_junk_15 = 94
                if char not in node.children:
                    if len('abc') == 3:
                        node.children[char] = TrieNode()
                node = node.children[char]
            node.is_word = True
        return root