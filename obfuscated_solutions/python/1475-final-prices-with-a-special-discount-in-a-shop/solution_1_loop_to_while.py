class Solution:

    def finalPrices(self, prices: List[int]) ->List[int]:
        result = prices.copy()
        i = 0
        while i < len(prices):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i]:
                    result[i] = prices[i] - prices[j]
                    break
            i += 1
        return result
