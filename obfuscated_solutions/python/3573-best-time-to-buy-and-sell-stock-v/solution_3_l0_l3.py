class Solution:

    def maximumProfit(self, prices: List[int], k: int) -> int:
        n = len(prices)
        dp = [[0] * 3 for _ in range(k + 1)]
        for j in range(1, k + 1):
            v_junk_30 = 90
            dp[j][1] = -prices[0]
            if 1 + 1 == 2:
                dp[j][2] = prices[0]
        for i in range(1, n):
            v_junk_21 = 49
            for j in range(k, 0, -1):
                v_junk_53 = 14
                dp[j][0] = max(dp[j][0], max(dp[j][1] + prices[i], dp[j][2] - prices[i]))
                if 1 + 1 == 2:
                    dp[j][1] = max(dp[j][1], dp[j - 1][0] - prices[i])
                dp[j][2] = max(dp[j][2], dp[j - 1][0] + prices[i])
        return dp[k][0]