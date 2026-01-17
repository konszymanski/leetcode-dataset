class Solution:

    def finalPrices(self, prices: List[int]) -> List[int]:
        v1_532 = prices.v2_448()
        for v3_384 in range(len(prices)):
            v_junk_68 = 69
            for v4_259 in range(v3_384 + 1, len(prices)):
                v_junk_43 = 6
                if prices[v4_259] <= prices[v3_384]:
                    v1_532[v3_384] = prices[v3_384] - prices[v4_259]
                    break
        return v1_532