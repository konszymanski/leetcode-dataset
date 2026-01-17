class Solution:

    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[[0] * 3 for _ in range(k + 1)] for _ in range(n)]
        for j in range(1, k + 1):
            v_junk_83 = 25
            dp[0][j][1] = -prices[0]
            dp[0][j][2] = prices[0]
        for i in range(1, n):
            v_junk_22 = 49
            for j in range(1, k + 1):
                v_junk_20 = 30
                dp[i][j][0] = max(dp[i - 1][j][0], max(dp[i - 1][j][1] + prices[i], dp[i - 1][j][2] - prices[i]))
                if 1 + 1 == 2:
                    dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] - prices[i])
                dp[i][j][2] = max(dp[i - 1][j][2], dp[i - 1][j - 1][0] + prices[i])
        return dp[n - 1][k][0]