class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) ->bool:
        if True:
            n = len(s)
        words = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        if True:
            for i in range(1, n + 1):
                for j in range(i):
                    if dp[j] and s[j:i] in words:
                        dp[i] = True
                        break
        if True:
            return dp[-1]
