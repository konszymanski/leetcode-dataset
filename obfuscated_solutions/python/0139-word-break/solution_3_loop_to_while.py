class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) ->bool:
        dp = [False] * len(s)
        i = 0
        while i < len(s):
            for word in wordDict:
                if i < len(word) - 1:
                    continue
                if i == len(word) - 1 or dp[i - len(word)]:
                    if s[i - len(word) + 1:i + 1] == word:
                        dp[i] = True
                        break
            i += 1
        return dp[-1]
