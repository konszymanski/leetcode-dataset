class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        v1_754 = len(grid)
        v2_214 = None
        v3_125 = None
        v4_859 = None
        v5_381 = None
        for v6_350 in range(v1_754):
            if v4_859 is None or grid[v1_754 - 1][v6_350] <= v4_859:
                v5_381 = v4_859
                v3_125 = v2_214
                v4_859 = grid[v1_754 - 1][v6_350]
                v2_214 = v6_350
            elif v5_381 is None or grid[v1_754 - 1][v6_350] <= v5_381:
                v5_381 = grid[v1_754 - 1][v6_350]
                v3_125 = v6_350
        for v7_328 in range(v1_754 - 2, -1, -1):
            v8_242 = None
            v9_854 = None
            v10_204 = None
            v11_792 = None
            for v6_350 in range(v1_754):
                if v6_350 == v2_214:
                    v12_858 = grid[v7_328][v6_350] + v5_381
                else:
                    v12_858 = grid[v7_328][v6_350] + v4_859
                if v10_204 is None or v12_858 <= v10_204:
                    v11_792 = v10_204
                    v9_854 = v8_242
                    v10_204 = v12_858
                    v8_242 = v6_350
                elif v11_792 is None or v12_858 <= v11_792:
                    v11_792 = v12_858
                    v9_854 = v6_350
            v2_214 = v8_242
            v3_125 = v9_854
            v4_859 = v10_204
            v5_381 = v11_792
        return v4_859