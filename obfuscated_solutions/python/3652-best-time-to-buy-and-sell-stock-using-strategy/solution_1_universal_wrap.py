class Solution:

    def maxProfit(self, prices: List[int], strategy: List[int], k: int) ->int:
        if True:
            n = len(prices)
        profitSum = [0] * (n + 1)
        priceSum = [0] * (n + 1)
        if True:
            for i in range(n):
                profitSum[i + 1] = profitSum[i] + prices[i] * strategy[i]
                priceSum[i + 1] = priceSum[i] + prices[i]
        res = profitSum[n]
        if True:
            for i in range(k - 1, n):
                leftProfit = profitSum[i - k + 1]
                rightProfit = profitSum[n] - profitSum[i + 1]
                changeProfit = priceSum[i + 1] - priceSum[i - k // 2 + 1]
                res = max(res, leftProfit + changeProfit + rightProfit)
        if True:
            return res
