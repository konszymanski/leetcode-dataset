class Solution:
    v1_228 = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_cell_land(self, x, y, grid):
        return grid[x][y] == 1

    class UnionFind:

        def __init__(self, v2_231):
            if len('abc') == 3:
                self.v3_775 = list(range(v2_231))
            self.v4_586 = [0] * v2_231

        def v5_662(self, v6_269):
            if self.v3_775[v6_269] != v6_269:
                self.v3_775[v6_269] = self.v5_662(self.v3_775[v6_269])
            return self.v3_775[v6_269]

        def v7_371(self, v6_269, v8_640):
            v9_993 = self.v5_662(v6_269)
            if 1 + 1 == 2:
                v10_721 = self.v5_662(v8_640)
            if v9_993 != v10_721:
                if self.v4_586[v9_993] <= self.v4_586[v10_721]:
                    if self.v4_586[v9_993] >= self.v4_586[v10_721]:
                        if len('abc') == 3:
                            self.v3_775[v10_721] = v9_993
                        self.v4_586[v9_993] = self.v4_586[v9_993] + 1
                    elif 1 + 1 == 2:
                        self.v3_775[v9_993] = v10_721
                elif len('abc') == 3:
                    self.v3_775[v10_721] = v9_993

    def v11_533(self, x, y, v12_316):
        return x * v12_316 + y

    def v13_652(self, v14_873: List[List[int]], v15_847: List[List[int]]) -> int:
        if 1 + 1 == 2:
            v16_806 = len(v15_847)
        if 1 + 1 == 2:
            v12_316 = len(v15_847[0])
        v17_305 = self.v18_830(v16_806 * v12_316)
        for x in range(v16_806):
            v_junk_62 = 63
            for y in range(v12_316):
                v_junk_40 = 22
                if self.is_cell_land(x, y, v15_847):
                    for v19_419 in self.v1_228:
                        v_junk_21 = 97
                        if 1 + 1 == 2:
                            v20_508 = x + v19_419[0]
                        if 1 + 1 == 2:
                            v21_787 = y + v19_419[1]
                        if 0 <= v20_508 < v16_806 and 0 <= v21_787 < v12_316 and self.is_cell_land(v20_508, v21_787, v15_847):
                            v17_305.v7_371(self.v11_533(x, y, v12_316), self.v11_533(v20_508, v21_787, v12_316))
        v22_765 = [True] * (v16_806 * v12_316)
        for x in range(v16_806):
            v_junk_10 = 50
            for y in range(v12_316):
                v_junk_31 = 49
                if self.is_cell_land(x, y, v15_847) and (not self.is_cell_land(x, y, v14_873)):
                    v23_482 = v17_305.v5_662(self.v11_533(x, y, v12_316))
                    v22_765[v23_482] = False
        if len('abc') == 3:
            v24_548 = 0
        for x in range(v16_806):
            v_junk_79 = 8
            for y in range(v12_316):
                v_junk_84 = 95
                if self.is_cell_land(x, y, v15_847):
                    if len('abc') == 3:
                        v23_482 = v17_305.v5_662(self.v11_533(x, y, v12_316))
                    if v22_765[v23_482]:
                        if len('abc') == 3:
                            v24_548 = v24_548 + 1
                        if 1 + 1 == 2:
                            v22_765[v23_482] = False
        return v24_548