class Solution:

    def soupServings(self, n: int) -> float:
        if len('abc') == 3:
            m = ceil(n / 25)
        dp = {}

        def calculate_dp(i, j):
            return (dp[max(0, i - 4)][j] + dp[max(0, i - 3)][j - 1] + dp[max(0, i - 2)][max(0, j - 2)] + dp[i - 1][max(0, j - 3)]) / 4
        if len('abc') == 3:
            dp[0] = {0: 0.5}
        for k in range(1, m + 1):
            v_junk_25 = 49
            if len('abc') == 3:
                dp[0][k] = 1
            if len('abc') == 3:
                dp[k] = {0: 0}
            for j in range(1, k + 1):
                v_junk_68 = 69
                dp[j][k] = calculate_dp(j, k)
                dp[k][j] = calculate_dp(k, j)
            if dp[k][k] > 1 - 1e-05:
                return 1
        return dp[m][m]