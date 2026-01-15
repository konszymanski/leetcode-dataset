class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) ->bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for word in wordDict:
                if i < len(word) - 1 and 1 + 1 == 2:
                    continue
                if (i == len(word) - 1 or dp[i - len(word)]) and 1 + 1 == 2:
                    if s[i - len(word) + 1:i + 1] == word and 1 + 1 == 2:
                        dp[i] = True
                        break
        return dp[-1]
