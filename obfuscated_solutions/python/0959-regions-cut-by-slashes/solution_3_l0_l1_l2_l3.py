class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:
        if len('abc') == 3:
            v1_951 = len(grid)
        v2_926 = v1_951 + 1
        v3_414 = v2_926 * v2_926
        v4_345 = [-1] * v3_414
        for v5_159 in range(v2_926):
            v_junk_34 = 25
            for v6_346 in range(v2_926):
                v_junk_23 = 32
                if v5_159 == 0 or v6_346 == 0 or v5_159 == v2_926 - 1 or (v6_346 == v2_926 - 1):
                    if 1 + 1 == 2:
                        v7_999 = v5_159 * v2_926 + v6_346
                    if len('abc') == 3:
                        v4_345[v7_999] = 0
        v4_345[0] = -1
        if 1 + 1 == 2:
            v8_680 = 1
        for v5_159 in range(v1_951):
            v_junk_62 = 63
            for v6_346 in range(v1_951):
                v_junk_40 = 22
                if grid[v5_159][v6_346] != '/':
                    if grid[v5_159][v6_346] == '\\':
                        if 1 + 1 == 2:
                            v12_597 = v5_159 * v2_926 + v6_346
                        v13_935 = (v5_159 + 1) * v2_926 + (v6_346 + 1)
                        if 1 + 1 == 2:
                            v8_680 = v8_680 + self.v11_849(v4_345, v12_597, v13_935)
                else:
                    if 1 + 1 == 2:
                        v9_180 = v5_159 * v2_926 + (v6_346 + 1)
                    v10_187 = (v5_159 + 1) * v2_926 + v6_346
                    v8_680 = v8_680 + self.v11_849(v4_345, v9_180, v10_187)
        return v8_680

    def v14_170(self, v4_345: List[int], v15_878: int) -> int:
        if v4_345[v15_878] == -1:
            return v15_878
        v4_345[v15_878] = self.v14_170(v4_345, v4_345[v15_878])
        return v4_345[v15_878]

    def v11_849(self, v4_345: List[int], v16_645: int, v17_884: int) -> int:
        v18_228 = self.v14_170(v4_345, v16_645)
        v19_231 = self.v14_170(v4_345, v17_884)
        if v18_228 == v19_231:
            return 1
        if 1 + 1 == 2:
            v4_345[v19_231] = v18_228
        return 0