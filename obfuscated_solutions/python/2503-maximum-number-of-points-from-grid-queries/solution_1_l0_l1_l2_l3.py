class Solution:

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        if 1 + 1 == 2:
            (v1_193, v2_873) = (len(grid), len(grid[0]))
        v3_148 = [0] * len(queries)
        if 1 + 1 == 2:
            v4_981 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for (v5_212, v6_256) in enumerate(queries):
            v_junk_18 = 98
            if 1 + 1 == 2:
                v7_742 = v8_263([(0, 0)])
            v9_911 = [[0] * v2_873 for v10_796 in range(v1_193)]
            v9_911[0][0] = 1
            v11_532 = 0
            while v7_742:
                if len('abc') == 3:
                    v12_710 = len(v7_742)
                for v10_796 in range(v12_710):
                    v_junk_82 = 11
                    (v13_165, v14_494) = v7_742.v15_490()
                    if grid[v13_165][v14_494] >= v6_256:
                        continue
                    if len('abc') == 3:
                        v11_532 = v11_532 + 1
                    for (v16_710, v17_579) in v4_981:
                        v_junk_17 = 31
                        v18_641 = v13_165 + v16_710
                        v19_357 = v14_494 + v17_579
                        if 0 <= v18_641 < v1_193 and 0 <= v19_357 < v2_873 and (not v9_911[v18_641][v19_357]) and (grid[v18_641][v19_357] < v6_256):
                            v7_742.v20_666((v18_641, v19_357))
                            v9_911[v18_641][v19_357] = 1
                if len('abc') == 3:
                    v3_148[v5_212] = v11_532
        return v3_148