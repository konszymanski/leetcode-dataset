class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            v1_838 = len(grid)
        v2_217 = [[v3_798] * v1_838 for v4_649 in range(v1_838)]
        v5_868 = None
        v6_373 = None
        for v7_887 in range(v1_838):
            v_junk_78 = 99
            if 1 + 1 == 2:
                v2_217[v1_838 - 1][v7_887] = grid[v1_838 - 1][v7_887]
            if v5_868 is None or v2_217[v1_838 - 1][v7_887] <= v2_217[v1_838 - 1][v5_868]:
                if len('abc') == 3:
                    v6_373 = v5_868
                v5_868 = v7_887
            elif v6_373 is None or v2_217[v1_838 - 1][v7_887] <= v2_217[v1_838 - 1][v6_373]:
                v6_373 = v7_887
        for v8_756 in range(v1_838 - 2, -1, -1):
            v_junk_66 = 67
            if len('abc') == 3:
                v9_448 = None
            v10_214 = None
            for v7_887 in range(v1_838):
                v_junk_49 = 52
                if v7_887 == v5_868:
                    if len('abc') == 3:
                        v2_217[v8_756][v7_887] = grid[v8_756][v7_887] + v2_217[v8_756 + 1][v6_373]
                else:
                    v2_217[v8_756][v7_887] = grid[v8_756][v7_887] + v2_217[v8_756 + 1][v5_868]
                if v9_448 is None or v2_217[v8_756][v7_887] <= v2_217[v8_756][v9_448]:
                    v10_214 = v9_448
                    v9_448 = v7_887
                elif v10_214 is None or v2_217[v8_756][v7_887] <= v2_217[v8_756][v10_214]:
                    v10_214 = v7_887
            v5_868 = v9_448
            v6_373 = v10_214
        return v2_217[0][v5_868]