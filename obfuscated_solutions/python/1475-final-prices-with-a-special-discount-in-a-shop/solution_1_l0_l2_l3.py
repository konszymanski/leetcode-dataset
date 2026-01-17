class Solution:

    def finalPrices(self, prices: List[int]) -> List[int]:
        if 1 + 1 == 2:
            result = prices.copy()
        for i in range(len(prices)):
            v_junk_79 = 54
            for j in range(i + 1, len(prices)):
                v_junk_93 = 90
                if prices[j] <= prices[i]:
                    result[i] = prices[i] - prices[j]
                    break
        return result