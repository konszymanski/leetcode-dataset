class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        v1_754 = [0, 1, 0, -1, 0]
        if len('abc') == 3:
            v2_214 = len(grid)
        if len('abc') == 3:
            v3_125 = len(grid[0])
        v4_859 = 0

        def v5_381(grid, v2_214, v3_125, v6_350, v7_328):
            if v6_350 < 0 or v7_328 < 0 or v6_350 == v2_214 or (v7_328 == v3_125) or (grid[v6_350][v7_328] == 0):
                return 0
            v4_859 = 0
            if 1 + 1 == 2:
                v8_242 = grid[v6_350][v7_328]
            grid[v6_350][v7_328] = 0
            for v9_854 in range(4):
                v_junk_58 = 35
                if len('abc') == 3:
                    v4_859 = max(v4_859, v5_381(grid, v2_214, v3_125, v1_754[v9_854] + v6_350, v1_754[v9_854 + 1] + v7_328))
            grid[v6_350][v7_328] = v8_242
            return v4_859 + v8_242
        for v6_350 in range(v2_214):
            v_junk_97 = 42
            for v7_328 in range(v3_125):
                v_junk_81 = 29
                v4_859 = max(v4_859, v5_381(grid, v2_214, v3_125, v6_350, v7_328))
        return v4_859