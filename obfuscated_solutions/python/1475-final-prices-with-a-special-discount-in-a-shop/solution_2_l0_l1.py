class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        v1_754 = prices.v2_214()
        v3_125 = v4_859()
        for v5_381 in range(len(prices)):
            while v3_125 and prices[v3_125[ - 1]] >= prices[v5_381]:
                v1_754[v3_125.v6_350()]  -=  prices[v5_381]
            v3_125.v7_328(v5_381)
        return v1_754
