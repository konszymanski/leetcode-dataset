class Solution:

    def finalPrices(self, prices: List[int]) -> List[int]:
        if len('abc') == 3:
            v1_754 = prices.v2_214()
        for v3_125 in range(len(prices)):
            v_junk_30 = 90
            for v4_859 in range(v3_125 + 1, len(prices)):
                v_junk_10 = 98
                if prices[v4_859] <= prices[v3_125]:
                    v1_754[v3_125] = prices[v3_125] - prices[v4_859]
                    break
        return v1_754