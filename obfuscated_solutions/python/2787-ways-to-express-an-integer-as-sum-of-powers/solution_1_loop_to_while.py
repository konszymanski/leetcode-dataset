class Solution:

    def numberOfWays(self, n: int, x: int) ->int:
        MOD = 10 ** 9 + 7
        dp = [([0] * (n + 1)) for _ in range(n + 1)]
        dp[0][0] = 1
        i = 1
        while i < n + 1:
            val = i ** x
            for j in range(n + 1):
                dp[i][j] = dp[i - 1][j]
                if j >= val:
                    dp[i][j] = (dp[i][j] + dp[i - 1][j - val]) % MOD
            i += 1
        return dp[n][n]
