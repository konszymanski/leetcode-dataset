class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        v1_754 = len(grid)
        v2_214 = [[v3_125] * v1_754 for v4_859 in range(v1_754)]
        v5_381 = None
        v6_350 = None
        for v7_328 in range(v1_754):
            v2_214[v1_754 - 1][v7_328] = grid[v1_754 - 1][v7_328]
            if v5_381 is None or v2_214[v1_754 - 1][v7_328] <= v2_214[v1_754 - 1][v5_381]:
                v6_350 = v5_381
                v5_381 = v7_328
            elif v6_350 is None or v2_214[v1_754 - 1][v7_328] <= v2_214[v1_754 - 1][v6_350]:
                v6_350 = v7_328
        for v8_242 in range(v1_754 - 2, -1, -1):
            v9_854 = None
            v10_204 = None
            for v7_328 in range(v1_754):
                if v7_328 == v5_381:
                    v2_214[v8_242][v7_328] = grid[v8_242][v7_328] + v2_214[v8_242 + 1][v6_350]
                else:
                    v2_214[v8_242][v7_328] = grid[v8_242][v7_328] + v2_214[v8_242 + 1][v5_381]
                if v9_854 is None or v2_214[v8_242][v7_328] <= v2_214[v8_242][v9_854]:
                    v10_204 = v9_854
                    v9_854 = v7_328
                elif v10_204 is None or v2_214[v8_242][v7_328] <= v2_214[v8_242][v10_204]:
                    v10_204 = v7_328
            v5_381 = v9_854
            v6_350 = v10_204
        return v2_214[0][v5_381]