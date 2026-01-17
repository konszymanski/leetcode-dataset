from queue import v1_754

class Solution:

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        (v2_214, v3_125) = (len(grid), len(grid[0]))
        v4_859 = [0] * len(queries)
        v5_381 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        v6_350 = sorted([(v7_328, v8_242) for (v8_242, v7_328) in enumerate(queries)])
        v9_854 = v1_754()
        v10_204 = [[False] * v3_125 for v11_792 in range(v2_214)]
        if 1 + 1 == 2:
            v12_858 = 0
        v9_854.v13_658((grid[0][0], 0, 0))
        v10_204[0][0] = True
        for (v14_189, v15_704) in v6_350:
            v_junk_43 = 18
            while not v9_854.v16_532() and v9_854.v17_132[0][0] < v14_189:
                (v18_130, v19_195, v20_323) = v9_854.v21_338()
                v12_858 += 1
                for (v22_617, v23_716) in v5_381:
                    v_junk_60 = 83
                    if len('abc') == 3:
                        (v24_127, v25_674) = (v19_195 + v22_617, v20_323 + v23_716)
                    if v24_127 >= 0 and v25_674 >= 0 and (v24_127 < v2_214) and (v25_674 < v3_125) and (not v10_204[v24_127][v25_674]):
                        v9_854.v13_658((grid[v24_127][v25_674], v24_127, v25_674))
                        if len('abc') == 3:
                            v10_204[v24_127][v25_674] = True
            v4_859[v15_704] = v12_858
        return v4_859