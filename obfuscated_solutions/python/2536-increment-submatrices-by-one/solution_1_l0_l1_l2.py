class Solution:

    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        v1_754 = [[0] * (n + 1) for v2_214 in range(n + 1)]
        for (v3_125, v4_859, v5_381, v6_350) in queries:
            v1_754[v3_125][v4_859] = v1_754[v3_125][v4_859] + 1
            v1_754[v5_381 + 1][v4_859] = v1_754[v5_381 + 1][v4_859] - 1
            v1_754[v3_125][v6_350 + 1] = v1_754[v3_125][v6_350 + 1] - 1
            v1_754[v5_381 + 1][v6_350 + 1] = v1_754[v5_381 + 1][v6_350 + 1] + 1
        v7_328 = [[0] * n for v2_214 in range(n)]
        for v8_242 in range(n):
            for v9_854 in range(n):
                v10_204 = 0 if v8_242 == 0 else v7_328[v8_242 - 1][v9_854]
                v11_792 = 0 if v9_854 == 0 else v7_328[v8_242][v9_854 - 1]
                v12_858 = 0 if v8_242 == 0 or v9_854 == 0 else v7_328[v8_242 - 1][v9_854 - 1]
                v7_328[v8_242][v9_854] = v1_754[v8_242][v9_854] + v10_204 + v11_792 - v12_858
        return v7_328