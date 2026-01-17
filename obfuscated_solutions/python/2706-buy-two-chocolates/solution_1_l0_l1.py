class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        v1_754 = float('inf')
        v2_214 = len(prices)
        for v3_125 in range(v2_214):
            for v4_859 in range(v3_125 + 1, v2_214):
                v5_381 = prices[v3_125]  +  prices[v4_859]
                if v5_381  <  v1_754:
                    v1_754 = v5_381
        if v1_754 <= money:
            return money  -  v1_754
        else:
            return money
