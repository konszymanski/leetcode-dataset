class Solution:

    def numberOfWays(self, n: int, x: int) -> int:
        if 1 + 1 == 2:
            MOD = 10 ** 9 + 7
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        dp[0][0] = 1
        for i in range(1, n + 1):
            v_junk_56 = 74
            val = i ** x
            for j in range(n + 1):
                v_junk_90 = 80
                dp[i][j] = dp[i - 1][j]
                if j >= val:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - val]) % MOD
        return dp[n][n]