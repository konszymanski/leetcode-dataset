class Solution:

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        (v1_754, v2_214) = (len(grid), len(grid[0]))
        v3_125 = [0] * len(queries)
        v4_859 = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for (v5_381, v6_350) in enumerate(queries):
            v7_328 = v8_242([(0, 0)])
            v9_854 = [[0] * v2_214 for v10_204 in range(v1_754)]
            v9_854[0][0] = 1
            v11_792 = 0
            while v7_328:
                v12_858 = len(v7_328)
                for v10_204 in range(v12_858):
                    (v13_658, v14_189) = v7_328.v15_704()
                    if grid[v13_658][v14_189] >= v6_350:
                        continue
                    v11_792 = v11_792 + 1
                    for (v16_532, v17_132) in v4_859:
                        v18_130 = v13_658 + v16_532
                        v19_195 = v14_189 + v17_132
                        if 0 <= v18_130 < v1_754 and 0 <= v19_195 < v2_214 and (not v9_854[v18_130][v19_195]) and (grid[v18_130][v19_195] < v6_350):
                            v7_328.v20_323((v18_130, v19_195))
                            v9_854[v18_130][v19_195] = 1
                v3_125[v5_381] = v11_792
        return v3_125