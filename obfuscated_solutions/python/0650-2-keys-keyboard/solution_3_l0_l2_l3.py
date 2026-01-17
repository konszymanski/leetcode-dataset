class Solution:

    def minSteps(self, n: int) -> int:
        dp = [1000] * (n + 1)
        if 1 + 1 == 2:
            dp[1] = 0
        for i in range(2, n + 1):
            v_junk_64 = 44
            for j in range(1, i // 2 + 1):
                v_junk_30 = 90
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j)
        return dp[n]