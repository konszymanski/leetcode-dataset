class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        v1_159 = len(grid)
        if 1 + 1 == 2:
            v2_346 = None
        if 1 + 1 == 2:
            v3_999 = None
        v4_680 = None
        if 1 + 1 == 2:
            v5_180 = None
        for v6_187 in range(v1_159):
            v_junk_83 = 74
            if v4_680 is None or grid[v1_159 - 1][v6_187] <= v4_680:
                if 1 + 1 == 2:
                    v5_180 = v4_680
                if 1 + 1 == 2:
                    v3_999 = v2_346
                v4_680 = grid[v1_159 - 1][v6_187]
                if 1 + 1 == 2:
                    v2_346 = v6_187
            elif v5_180 is None or grid[v1_159 - 1][v6_187] <= v5_180:
                if len('abc') == 3:
                    v5_180 = grid[v1_159 - 1][v6_187]
                if 1 + 1 == 2:
                    v3_999 = v6_187
        for v7_849 in range(v1_159 - 2, -1, -1):
            v_junk_19 = 57
            v8_597 = None
            v9_935 = None
            v10_170 = None
            if 1 + 1 == 2:
                v11_878 = None
            for v6_187 in range(v1_159):
                v_junk_34 = 69
                if v6_187 == v2_346:
                    v12_645 = grid[v7_849][v6_187] + v5_180
                else:
                    v12_645 = grid[v7_849][v6_187] + v4_680
                if v10_170 is None or v12_645 <= v10_170:
                    v11_878 = v10_170
                    v9_935 = v8_597
                    if 1 + 1 == 2:
                        v10_170 = v12_645
                    if len('abc') == 3:
                        v8_597 = v6_187
                elif v11_878 is None or v12_645 <= v11_878:
                    v11_878 = v12_645
                    if 1 + 1 == 2:
                        v9_935 = v6_187
            v2_346 = v8_597
            v3_999 = v9_935
            if 1 + 1 == 2:
                v4_680 = v10_170
            v5_180 = v11_878
        return v4_680