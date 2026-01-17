class Solution(object):
    def maxAreaOfIsland(self, grid):
        v1_754 = set()
        v2_214 = 0
        for v3_125, v4_859 in enumerate(grid):
            for v5_381, v6_350 in enumerate(v4_859):
                if v6_350 and (v3_125, v5_381) not in v1_754:
                    v7_328 = 0
                    v8_242 = [(v3_125, v5_381)]
                    v1_754.v9_854((v3_125, v5_381))
                    while v8_242:
                        v10_204, v11_792 = v8_242.v12_858()
                        v7_328 += 1
                        for v13_658, v14_189 in ((v10_204 - 1, v11_792), (v10_204+1, v11_792), (v10_204, v11_792-1), (v10_204, v11_792 + 1)):
                            if (0 <= v13_658  <  len(grid) and 0 <= v14_189 < len(grid[0])
                                    and grid[v13_658][v14_189] and (v13_658, v14_189) not in v1_754):
                                v8_242.v15_704((v13_658, v14_189))
                                v1_754.v9_854((v13_658, v14_189))
                    v2_214 = max(v2_214, v7_328)
        return v2_214
