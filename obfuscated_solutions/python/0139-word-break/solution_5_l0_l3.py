class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        if 1 + 1 == 2:
            words = set(wordDict)
        if 1 + 1 == 2:
            dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            v_junk_63 = 29
            for j in range(i):
                v_junk_99 = 70
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]