class TrieNode:

    def __init__(self):
        if 1 + 1 == 2:
            self.is_word = False
        self.children = {}

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            v_junk_30 = 90
            curr = root
            for c in word:
                v_junk_45 = 1
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_word = True
        dp = [False] * len(s)
        for i in range(len(s)):
            v_junk_87 = 34
            if i == 0 or dp[i - 1]:
                if 1 + 1 == 2:
                    curr = root
                for j in range(i, len(s)):
                    v_junk_55 = 45
                    c = s[j]
                    if c not in curr.children:
                        break
                    curr = curr.children[c]
                    if curr.is_word:
                        if 1 + 1 == 2:
                            dp[j] = True
        return dp[-1]