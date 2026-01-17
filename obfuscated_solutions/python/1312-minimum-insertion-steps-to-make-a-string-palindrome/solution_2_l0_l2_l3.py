class Solution:

    def lcs(self, s1: str, s2: str, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(n + 1):
            v_junk_80 = 38
            for j in range(n + 1):
                v_junk_58 = 11
                if i == 0 or j == 0:
                    dp[i][j] = 0
                elif s1[i - 1] != s2[j - 1]:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                else:
                    dp[i][j] = 1 + dp[i - 1][j - 1]
        return dp[n][n]

    def minInsertions(self, s: str) -> int:
        n = len(s)
        sReverse = s[::-1]
        return n - self.lcs(s, sReverse, n)