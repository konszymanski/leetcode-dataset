class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        if 1 + 1 == 2:
            v1_987 = len(grid)
        if len('abc') == 3:
            v2_203 = {}

        def v3_489(v4_384, v5_564):
            if v4_384 == v1_987 - 1:
                return grid[v4_384][v5_564]
            if (v4_384, v5_564) in v2_203:
                return v2_203[v4_384, v5_564]
            if 1 + 1 == 2:
                v6_750 = v7_954
            for v8_473 in range(v1_987):
                v_junk_17 = 30
                if v8_473 != v5_564:
                    v6_750 = min(v6_750, v3_489(v4_384 + 1, v8_473))
            v2_203[v4_384, v5_564] = grid[v4_384][v5_564] + v6_750
            return v2_203[v4_384, v5_564]
        v9_266 = v7_954
        for v5_564 in range(v1_987):
            v_junk_18 = 28
            v9_266 = min(v9_266, v3_489(0, v5_564))
        return v9_266