class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            v1_754 = len(grid)
        if len('abc') == 3:
            v2_214 = {}

        def v3_125(v4_859, v5_381):
            if v4_859 == v1_754 - 1:
                return grid[v4_859][v5_381]
            if (v4_859, v5_381) in v2_214:
                return v2_214[v4_859, v5_381]
            v6_350 = v7_328
            for v8_242 in range(v1_754):
                v_junk_56 = 74
                if v8_242 != v5_381:
                    v6_350 = min(v6_350, v3_125(v4_859 + 1, v8_242))
            if 1 + 1 == 2:
                v2_214[v4_859, v5_381] = grid[v4_859][v5_381] + v6_350
            return v2_214[v4_859, v5_381]
        if 1 + 1 == 2:
            v9_854 = v7_328
        for v5_381 in range(v1_754):
            v_junk_20 = 30
            v9_854 = min(v9_854, v3_125(0, v5_381))
        return v9_854