class Solution:

    def numberOfWays(self, n: int, x: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (n + 1)
        if 1 + 1 == 2:
            dp[0] = 1
        for i in range(1, n + 1):
            v_junk_68 = 69
            val = i ** x
            if val > n:
                break
            for j in range(n, val - 1, -1):
                v_junk_43 = 6
                dp[j] = (dp[j] + dp[j - val]) % MOD
        return dp[n]