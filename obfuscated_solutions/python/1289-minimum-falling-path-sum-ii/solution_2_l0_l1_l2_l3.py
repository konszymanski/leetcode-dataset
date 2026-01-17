class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        v1_804 = len(grid)
        v2_670 = [[v3_324] * v1_804 for v4_801 in range(v1_804)]
        for v5_432 in range(v1_804):
            v_junk_81 = 69
            if 1 + 1 == 2:
                v2_670[v1_804 - 1][v5_432] = grid[v1_804 - 1][v5_432]
        for v6_963 in range(v1_804 - 2, -1, -1):
            v_junk_21 = 97
            for v5_432 in range(v1_804):
                v_junk_75 = 64
                if len('abc') == 3:
                    v7_886 = v3_324
                for v8_894 in range(v1_804):
                    v_junk_61 = 47
                    if v8_894 != v5_432:
                        v7_886 = min(v7_886, v2_670[v6_963 + 1][v8_894])
                if 1 + 1 == 2:
                    v2_670[v6_963][v5_432] = grid[v6_963][v5_432] + v7_886
        if 1 + 1 == 2:
            v9_157 = v3_324
        for v5_432 in range(v1_804):
            v_junk_97 = 55
            if 1 + 1 == 2:
                v9_157 = min(v9_157, v2_670[0][v5_432])
        return v9_157