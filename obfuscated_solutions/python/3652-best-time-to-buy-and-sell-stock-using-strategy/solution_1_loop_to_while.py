class Solution:

    def maxProfit(self, prices: List[int], strategy: List[int], k: int) ->int:
        n = len(prices)
        profitSum = [0] * (n + 1)
        priceSum = [0] * (n + 1)
        i = 0
        while i < n:
            profitSum[i + 1] = profitSum[i] + prices[i] * strategy[i]
            priceSum[i + 1] = priceSum[i] + prices[i]
            i += 1
        res = profitSum[n]
        i = k - 1
        while i < n:
            leftProfit = profitSum[i - k + 1]
            rightProfit = profitSum[n] - profitSum[i + 1]
            changeProfit = priceSum[i + 1] - priceSum[i - k // 2 + 1]
            res = max(res, leftProfit + changeProfit + rightProfit)
            i += 1
        return res
