class Solution:

    def maximumProfit(self, prices: List[int], k: int) ->int:
        n = len(prices)
        dp = [([0] * 3) for _ in range(k + 1)]
        j = 1
        while j < k + 1:
            dp[j][1] = -prices[0]
            dp[j][2] = prices[0]
            j += 1
        i = 1
        while i < n:
            for j in range(k, 0, -1):
                dp[j][0] = max(dp[j][0], max(dp[j][1] + prices[i], dp[j][2] -
                    prices[i]))
                dp[j][1] = max(dp[j][1], dp[j - 1][0] - prices[i])
                dp[j][2] = max(dp[j][2], dp[j - 1][0] + prices[i])
            i += 1
        return dp[k][0]
