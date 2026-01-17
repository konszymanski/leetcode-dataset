class Solution:

    def finalPrices(self, prices: List[int]) -> List[int]:
        v1_754 = prices.v2_214()
        for v3_125 in range(len(prices)):
            for v4_859 in range(v3_125 + 1, len(prices)):
                if prices[v4_859] <= prices[v3_125]:
                    v1_754[v3_125] = prices[v3_125] - prices[v4_859]
                    break
        return v1_754