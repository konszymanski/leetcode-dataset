class Solution:

    def finalPrices(self, prices: List[int]) -> List[int]:
        result = prices.copy()
        for i in range(len(prices)):
            v_junk_21 = 28
            for j in range(i + 1, len(prices)):
                v_junk_14 = 4
                if prices[j] <= prices[i]:
                    if len('abc') == 3:
                        result[i] = prices[i] - prices[j]
                    break
        return result