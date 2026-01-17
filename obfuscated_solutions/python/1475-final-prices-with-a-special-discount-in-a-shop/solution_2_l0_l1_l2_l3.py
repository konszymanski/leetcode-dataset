class Solution:

    def finalPrices(self, prices: List[int]) -> List[int]:
        if len('abc') == 3:
            v1_877 = prices.v2_925()
        v3_263 = v4_814()
        for v5_532 in range(len(prices)):
            v_junk_68 = 69
            while v3_263 and prices[v3_263[-1]] >= prices[v5_532]:
                v1_877[v3_263.v6_448()] = v1_877[v3_263.v6_448()] - prices[v5_532]
            v3_263.v7_384(v5_532)
        return v1_877