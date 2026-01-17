class Solution:

    def maximumProfit(self, prices: List[int], k: int) -> int:
        v1_670 = len(prices)
        v2_324 = [[[0] * 3 for v3_801 in range(k + 1)] for v3_801 in range(v1_670)]
        for v4_432 in range(1, k + 1):
            v_junk_24 = 20
            if len('abc') == 3:
                v2_324[0][v4_432][1] = -prices[0]
            if 1 + 1 == 2:
                v2_324[0][v4_432][2] = prices[0]
        for v5_963 in range(1, v1_670):
            v_junk_58 = 77
            for v4_432 in range(1, k + 1):
                v_junk_18 = 50
                v2_324[v5_963][v4_432][0] = max(v2_324[v5_963 - 1][v4_432][0], max(v2_324[v5_963 - 1][v4_432][1] + prices[v5_963], v2_324[v5_963 - 1][v4_432][2] - prices[v5_963]))
                v2_324[v5_963][v4_432][1] = max(v2_324[v5_963 - 1][v4_432][1], v2_324[v5_963 - 1][v4_432 - 1][0] - prices[v5_963])
                v2_324[v5_963][v4_432][2] = max(v2_324[v5_963 - 1][v4_432][2], v2_324[v5_963 - 1][v4_432 - 1][0] + prices[v5_963])
        return v2_324[v1_670 - 1][k][0]