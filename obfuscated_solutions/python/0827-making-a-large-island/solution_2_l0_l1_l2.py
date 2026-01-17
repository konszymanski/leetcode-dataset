class DisjointSet:

    def __init__(self, v1_754: int):
        self.v2_214 = [v3_125 for v3_125 in range(v1_754)]
        self.v4_859 = [1] * v1_754

    def v5_381(self, v6_350: int) -> int:
        if self.v2_214[v6_350] == v6_350:
            return v6_350
        self.v2_214[v6_350] = self.v5_381(self.v2_214[v6_350])
        return self.v2_214[v6_350]

    def v7_328(self, v8_242: int, v9_854: int):
        v10_204 = self.v5_381(v8_242)
        v11_792 = self.v5_381(v9_854)
        if v10_204 == v11_792:
            return
        if self.v4_859[v10_204] >= self.v4_859[v11_792]:
            self.v2_214[v11_792] = v10_204
            self.v4_859[v10_204] = self.v4_859[v10_204] + self.v4_859[v11_792]
        else:
            self.v2_214[v10_204] = v11_792
            self.v4_859[v11_792] = self.v4_859[v11_792] + self.v4_859[v10_204]

class Solution:

    def largestIsland(self, grid: list[list[int]]) -> int:
        v12_858 = len(grid)
        v13_658 = len(grid[0])
        v14_189 = v15_704(v12_858 * v13_658)
        v16_532 = [1, -1, 0, 0]
        v17_132 = [0, 0, 1, -1]
        for v18_130 in range(v12_858):
            for v19_195 in range(v13_658):
                if grid[v18_130][v19_195] == 1:
                    v20_323 = v13_658 * v18_130 + v19_195
                    for v21_338 in range(4):
                        v22_617 = v18_130 + v16_532[v21_338]
                        v23_716 = v19_195 + v17_132[v21_338]
                        if 0 <= v22_617 < v12_858 and 0 <= v23_716 < v13_658 and (grid[v22_617][v23_716] == 1):
                            v24_127 = v13_658 * v22_617 + v23_716
                            v14_189.v7_328(v20_323, v24_127)
        v25_674 = 0
        v26_303 = False
        v27_833 = set()
        for v18_130 in range(v12_858):
            for v19_195 in range(v13_658):
                if grid[v18_130][v19_195] == 0:
                    v26_303 = True
                    v28_765 = 1
                    for v21_338 in range(4):
                        v22_617 = v18_130 + v16_532[v21_338]
                        v23_716 = v19_195 + v17_132[v21_338]
                        if 0 <= v22_617 < v12_858 and 0 <= v23_716 < v13_658 and (grid[v22_617][v23_716] == 1):
                            v24_127 = v13_658 * v22_617 + v23_716
                            v29_818 = v14_189.v5_381(v24_127)
                            v27_833.v30_658(v29_818)
                    for v29_818 in v27_833:
                        v28_765 = v28_765 + v14_189.v4_859[v29_818]
                    v27_833.v31_529()
                    v25_674 = max(v25_674, v28_765)
        if not v26_303:
            return v12_858 * v13_658
        return v25_674