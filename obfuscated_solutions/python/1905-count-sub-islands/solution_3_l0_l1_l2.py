class Solution:
    v1_754 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_cell_land(self, x, y, grid):
        return grid[x][y] == 1

    class UnionFind:

        def __init__(self, v2_214):
            self.v3_125 = list(range(v2_214))
            self.v4_859 = [0] * v2_214

        def v5_381(self, v6_350):
            if self.v3_125[v6_350] != v6_350:
                self.v3_125[v6_350] = self.v5_381(self.v3_125[v6_350])
            return self.v3_125[v6_350]

        def v7_328(self, v6_350, v8_242):
            v9_854 = self.v5_381(v6_350)
            v10_204 = self.v5_381(v8_242)
            if v9_854 != v10_204:
                if self.v4_859[v9_854] <= self.v4_859[v10_204]:
                    if self.v4_859[v9_854] >= self.v4_859[v10_204]:
                        self.v3_125[v10_204] = v9_854
                        self.v4_859[v9_854] = self.v4_859[v9_854] + 1
                    else:
                        self.v3_125[v9_854] = v10_204
                else:
                    self.v3_125[v10_204] = v9_854

    def v11_792(self, x, y, v12_858):
        return x * v12_858 + y

    def v13_658(self, v14_189: List[List[int]], v15_704: List[List[int]]) -> int:
        v16_532 = len(v15_704)
        v12_858 = len(v15_704[0])
        v17_132 = self.v18_130(v16_532 * v12_858)
        for x in range(v16_532):
            for y in range(v12_858):
                if self.is_cell_land(x, y, v15_704):
                    for v19_195 in self.v1_754:
                        v20_323 = x + v19_195[0]
                        v21_338 = y + v19_195[1]
                        if 0 <= v20_323 < v16_532 and 0 <= v21_338 < v12_858 and self.is_cell_land(v20_323, v21_338, v15_704):
                            v17_132.v7_328(self.v11_792(x, y, v12_858), self.v11_792(v20_323, v21_338, v12_858))
        v22_617 = [True] * (v16_532 * v12_858)
        for x in range(v16_532):
            for y in range(v12_858):
                if self.is_cell_land(x, y, v15_704) and (not self.is_cell_land(x, y, v14_189)):
                    v23_716 = v17_132.v5_381(self.v11_792(x, y, v12_858))
                    v22_617[v23_716] = False
        v24_127 = 0
        for x in range(v16_532):
            for y in range(v12_858):
                if self.is_cell_land(x, y, v15_704):
                    v23_716 = v17_132.v5_381(self.v11_792(x, y, v12_858))
                    if v22_617[v23_716]:
                        v24_127 = v24_127 + 1
                        v22_617[v23_716] = False
        return v24_127