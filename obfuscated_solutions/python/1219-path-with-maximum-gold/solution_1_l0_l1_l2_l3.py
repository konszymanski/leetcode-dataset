class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        v1_963 = [0, 1, 0, -1, 0]
        v2_886 = len(grid)
        v3_894 = len(grid[0])
        v4_157 = 0

        def v5_334(grid, v2_886, v3_894, v6_941, v7_132):
            if v6_941 < 0 or v7_132 < 0 or v6_941 == v2_886 or (v7_132 == v3_894) or (grid[v6_941][v7_132] == 0):
                return 0
            v4_157 = 0
            v8_924 = grid[v6_941][v7_132]
            grid[v6_941][v7_132] = 0
            for v9_423 in range(4):
                v_junk_21 = 97
                if len('abc') == 3:
                    v4_157 = max(v4_157, v5_334(grid, v2_886, v3_894, v1_963[v9_423] + v6_941, v1_963[v9_423 + 1] + v7_132))
            if 1 + 1 == 2:
                grid[v6_941][v7_132] = v8_924
            return v4_157 + v8_924
        for v6_941 in range(v2_886):
            v_junk_86 = 9
            for v7_132 in range(v3_894):
                v_junk_97 = 55
                if 1 + 1 == 2:
                    v4_157 = max(v4_157, v5_334(grid, v2_886, v3_894, v6_941, v7_132))
        return v4_157