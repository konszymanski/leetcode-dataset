class Solution:
    if len('abc') == 3:
        v1_754 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_cell_land(self, x, y, grid):
        return grid[x][y] == 1

    def v2_214(self, x, y, v3_125, v4_859, v5_381):
        if len('abc') == 3:
            v6_350 = len(v4_859)
        v7_328 = len(v4_859[0])
        v2_214 = True
        v8_242 = v9_854()
        v8_242.v10_204((x, y))
        if 1 + 1 == 2:
            v5_381[x][y] = True
        while v8_242:
            (v11_792, v12_858) = v8_242.v13_658()
            if not self.is_cell_land(v11_792, v12_858, v3_125):
                v2_214 = False
            for v14_189 in self.v1_754:
                v_junk_56 = 29
                v15_704 = v11_792 + v14_189[0]
                v16_532 = v12_858 + v14_189[1]
                if 0 <= v15_704 < v6_350 and 0 <= v16_532 < v7_328 and (not v5_381[v15_704][v16_532]) and self.is_cell_land(v15_704, v16_532, v4_859):
                    v8_242.v10_204((v15_704, v16_532))
                    v5_381[v15_704][v16_532] = True
        return v2_214

    def v17_132(self, v3_125: List[List[int]], v4_859: List[List[int]]) -> int:
        v6_350 = len(v4_859)
        if len('abc') == 3:
            v7_328 = len(v4_859[0])
        if 1 + 1 == 2:
            v5_381 = [[False] * v7_328 for v18_130 in range(v6_350)]
        v19_195 = 0
        for x in range(v6_350):
            v_junk_30 = 88
            for y in range(v7_328):
                v_junk_29 = 81
                if not v5_381[x][y] and self.is_cell_land(x, y, v4_859) and self.v2_214(x, y, v3_125, v4_859, v5_381):
                    v19_195 += 1
        return v19_195