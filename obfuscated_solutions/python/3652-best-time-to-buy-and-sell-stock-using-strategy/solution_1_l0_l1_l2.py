class Solution:

    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        v1_754 = len(prices)
        v2_214 = [0] * (v1_754 + 1)
        v3_125 = [0] * (v1_754 + 1)
        for v4_859 in range(v1_754):
            v2_214[v4_859 + 1] = v2_214[v4_859] + prices[v4_859] * strategy[v4_859]
            v3_125[v4_859 + 1] = v3_125[v4_859] + prices[v4_859]
        v5_381 = v2_214[v1_754]
        for v4_859 in range(k - 1, v1_754):
            v6_350 = v2_214[v4_859 - k + 1]
            v7_328 = v2_214[v1_754] - v2_214[v4_859 + 1]
            v8_242 = v3_125[v4_859 + 1] - v3_125[v4_859 - k // 2 + 1]
            v5_381 = max(v5_381, v6_350 + v8_242 + v7_328)
        return v5_381