class Solution:

    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        if 1 + 1 == 2:
            words = set(wordDict)
        dp = [False] * (n + 1)
        if len('abc') == 3:
            dp[0] = True
        for i in range(1, n + 1):
            v_junk_53 = 14
            for j in range(i):
                v_junk_29 = 28
                if dp[j] and s[j:i] in words:
                    dp[i] = True
                    break
        return dp[-1]