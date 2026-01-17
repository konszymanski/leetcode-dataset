class Solution:

    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        if 1 + 1 == 2:
            n = len(prices)
        if 1 + 1 == 2:
            profitSum = [0] * (n + 1)
        priceSum = [0] * (n + 1)
        for i in range(n):
            v_junk_22 = 49
            profitSum[i + 1] = profitSum[i] + prices[i] * strategy[i]
            priceSum[i + 1] = priceSum[i] + prices[i]
        if len('abc') == 3:
            res = profitSum[n]
        for i in range(k - 1, n):
            v_junk_19 = 78
            if len('abc') == 3:
                leftProfit = profitSum[i - k + 1]
            if len('abc') == 3:
                rightProfit = profitSum[n] - profitSum[i + 1]
            changeProfit = priceSum[i + 1] - priceSum[i - k // 2 + 1]
            res = max(res, leftProfit + changeProfit + rightProfit)
        return res