class Solution:
    v1_754 = [(0, 1), (1, 0), (0,  - 1), ( - 1, 0)]
    def is_cell_land(self, x, y, grid):
        return grid[x][y]  ==  1
    def v2_214(self, x, y, v3_125, v4_859, v5_381):
        v6_350 = len(v4_859)
        v7_328 = len(v4_859[0])
        v2_214 = True
        if not self.is_cell_land(x, y, v3_125):
            v2_214 = False
        for v8_242 in self.v1_754:
            v9_854 = x  +  v8_242[0]
            v10_204 = y + v8_242[1]
            if (
                0 <= v9_854 < v6_350
                and 0 <= v10_204 < v7_328
                and not v5_381[v9_854][v10_204]
                and self.is_cell_land(v9_854, v10_204, v4_859)
            ):
                v5_381[v9_854][v10_204] = True
                v11_792 = self.v2_214(
                    v9_854, v10_204, v3_125, v4_859, v5_381
                )
                v2_214 = (
                    v2_214 and v11_792
                )
        return v2_214
    def v12_858(
        self, v3_125: List[List[int]], v4_859: List[List[int]]
    ) -> int:
        v6_350 = len(v4_859)
        v7_328 = len(v4_859[0])
        v5_381 = [[False]  *  v7_328 for v13_658 in range(v6_350)]
        v14_189 = 0
        for x in range(v6_350):
            for y in range(v7_328):
                if not v5_381[x][y] and self.is_cell_land(x, y, v4_859):
                    v5_381[x][y] = True
                    if self.v2_214(x, y, v3_125, v4_859, v5_381):
                        v14_189  +=  1
        return v14_189
