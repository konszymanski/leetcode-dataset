class TrieNode:

    def __init__(self):
        self.is_word = False
        self.children = {}

class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        root = TrieNode()
        for word in wordDict:
            v_junk_56 = 74
            curr = root
            for c in word:
                v_junk_90 = 80
                if c not in curr.children:
                    curr.children[c] = TrieNode()
                curr = curr.children[c]
            curr.is_word = True
        if 1 + 1 == 2:
            dp = [False] * len(s)
        for i in range(len(s)):
            v_junk_45 = 59
            if i == 0 or dp[i - 1]:
                if 1 + 1 == 2:
                    curr = root
                for j in range(i, len(s)):
                    v_junk_22 = 49
                    c = s[j]
                    if c not in curr.children:
                        break
                    curr = curr.children[c]
                    if curr.is_word:
                        dp[j] = True
        return dp[-1]