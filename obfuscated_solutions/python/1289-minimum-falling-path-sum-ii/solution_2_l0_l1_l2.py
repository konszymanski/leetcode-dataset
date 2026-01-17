class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        v1_754 = len(grid)
        v2_214 = [[v3_125] * v1_754 for v4_859 in range(v1_754)]
        for v5_381 in range(v1_754):
            v2_214[v1_754 - 1][v5_381] = grid[v1_754 - 1][v5_381]
        for v6_350 in range(v1_754 - 2, -1, -1):
            for v5_381 in range(v1_754):
                v7_328 = v3_125
                for v8_242 in range(v1_754):
                    if v8_242 != v5_381:
                        v7_328 = min(v7_328, v2_214[v6_350 + 1][v8_242])
                v2_214[v6_350][v5_381] = grid[v6_350][v5_381] + v7_328
        v9_854 = v3_125
        for v5_381 in range(v1_754):
            v9_854 = min(v9_854, v2_214[0][v5_381])
        return v9_854