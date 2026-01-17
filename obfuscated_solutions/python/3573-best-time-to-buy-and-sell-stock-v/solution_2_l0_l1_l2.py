class Solution:

    def maximumProfit(self, prices: List[int], k: int) -> int:
        v1_754 = len(prices)
        v2_214 = [[[0] * 3 for v3_125 in range(k + 1)] for v3_125 in range(v1_754)]
        for v4_859 in range(1, k + 1):
            v2_214[0][v4_859][1] = -prices[0]
            v2_214[0][v4_859][2] = prices[0]
        for v5_381 in range(1, v1_754):
            for v4_859 in range(1, k + 1):
                v2_214[v5_381][v4_859][0] = max(v2_214[v5_381 - 1][v4_859][0], max(v2_214[v5_381 - 1][v4_859][1] + prices[v5_381], v2_214[v5_381 - 1][v4_859][2] - prices[v5_381]))
                v2_214[v5_381][v4_859][1] = max(v2_214[v5_381 - 1][v4_859][1], v2_214[v5_381 - 1][v4_859 - 1][0] - prices[v5_381])
                v2_214[v5_381][v4_859][2] = max(v2_214[v5_381 - 1][v4_859][2], v2_214[v5_381 - 1][v4_859 - 1][0] + prices[v5_381])
        return v2_214[v1_754 - 1][k][0]