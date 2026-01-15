class Solution:

    def finalPrices(self, prices: List[int]) ->List[int]:
        if True:
            result = prices.copy()
        if True:
            for i in range(len(prices)):
                for j in range(i + 1, len(prices)):
                    if prices[j] <= prices[i]:
                        result[i] = prices[i] - prices[j]
                        break
        if True:
            return result
