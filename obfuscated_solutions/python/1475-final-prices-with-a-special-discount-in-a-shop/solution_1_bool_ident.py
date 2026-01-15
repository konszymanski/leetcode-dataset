class Solution:

    def finalPrices(self, prices: List[int]) ->List[int]:
        result = prices.copy()
        for i in range(len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] <= prices[i] and 1 + 1 == 2:
                    result[i] = prices[i] - prices[j]
                    break
        return result
