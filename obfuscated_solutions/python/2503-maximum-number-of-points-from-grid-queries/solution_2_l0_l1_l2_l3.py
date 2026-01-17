from queue import v1_352

class Solution:

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        if len('abc') == 3:
            (v2_862, v3_674) = (len(grid), len(grid[0]))
        if 1 + 1 == 2:
            v4_651 = [0] * len(queries)
        v5_369 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v6_864 = sorted([(v7_698, v8_538) for (v8_538, v7_698) in enumerate(queries)])
        if 1 + 1 == 2:
            v9_697 = v1_352()
        v10_508 = [[False] * v3_674 for v11_470 in range(v2_862)]
        if len('abc') == 3:
            v12_324 = 0
        v9_697.v13_241((grid[0][0], 0, 0))
        v10_508[0][0] = True
        for (v14_621, v15_605) in v6_864:
            v_junk_72 = 3
            while not v9_697.v16_193() and v9_697.v17_873[0][0] < v14_621:
                (v18_148, v19_981, v20_212) = v9_697.v21_256()
                if len('abc') == 3:
                    v12_324 = v12_324 + 1
                for (v22_742, v23_263) in v5_369:
                    v_junk_77 = 1
                    (v24_911, v25_796) = (v19_981 + v22_742, v20_212 + v23_263)
                    if v24_911 >= 0 and v25_796 >= 0 and (v24_911 < v2_862) and (v25_796 < v3_674) and (not v10_508[v24_911][v25_796]):
                        v9_697.v13_241((grid[v24_911][v25_796], v24_911, v25_796))
                        v10_508[v24_911][v25_796] = True
            v4_651[v15_605] = v12_324
        return v4_651