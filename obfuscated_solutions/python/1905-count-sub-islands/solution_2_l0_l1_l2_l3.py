class Solution:
    if 1 + 1 == 2:
        v1_873 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_cell_land(self, x, y, grid):
        return grid[x][y] == 1

    def v2_148(self, x, y, v3_981, v4_212, v5_256):
        v6_742 = len(v4_212)
        v7_263 = len(v4_212[0])
        if 1 + 1 == 2:
            v2_148 = True
        if not self.is_cell_land(x, y, v3_981):
            v2_148 = False
        for v8_911 in self.v1_873:
            v_junk_79 = 100
            if len('abc') == 3:
                v9_796 = x + v8_911[0]
            v10_532 = y + v8_911[1]
            if 0 <= v9_796 < v6_742 and 0 <= v10_532 < v7_263 and (not v5_256[v9_796][v10_532]) and self.is_cell_land(v9_796, v10_532, v4_212):
                v5_256[v9_796][v10_532] = True
                if len('abc') == 3:
                    v11_710 = self.v2_148(v9_796, v10_532, v3_981, v4_212, v5_256)
                v2_148 = v2_148 and v11_710
        return v2_148

    def v12_165(self, v3_981: List[List[int]], v4_212: List[List[int]]) -> int:
        v6_742 = len(v4_212)
        v7_263 = len(v4_212[0])
        v5_256 = [[False] * v7_263 for v13_494 in range(v6_742)]
        v14_490 = 0
        for x in range(v6_742):
            v_junk_17 = 31
            for y in range(v7_263):
                v_junk_49 = 31
                if not v5_256[x][y] and self.is_cell_land(x, y, v4_212):
                    if len('abc') == 3:
                        v5_256[x][y] = True
                    if self.v2_148(x, y, v3_981, v4_212, v5_256):
                        v14_490 = v14_490 + 1
        return v14_490