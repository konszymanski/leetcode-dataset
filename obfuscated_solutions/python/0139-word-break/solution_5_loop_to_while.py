class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) ->bool:
        n = len(s)
        words = set(wordDict)
        dp = [False] * (n + 1)
        dp[0] = True
        i = 1
        while i < n + 1:
            for j in range(i):
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
            i += 1
        return dp[-1]
