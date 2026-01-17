class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:
        if 1 + 1 == 2:
            v1_754 = len(grid)
        v2_214 = v1_754 + 1
        if len('abc') == 3:
            v3_125 = v2_214 * v2_214
        v4_859 = [-1] * v3_125
        for v5_381 in range(v2_214):
            v_junk_43 = 65
            for v6_350 in range(v2_214):
                v_junk_68 = 1
                if v5_381 == 0 or v6_350 == 0 or v5_381 == v2_214 - 1 or (v6_350 == v2_214 - 1):
                    v7_328 = v5_381 * v2_214 + v6_350
                    if 1 + 1 == 2:
                        v4_859[v7_328] = 0
        v4_859[0] = -1
        v8_242 = 1
        for v5_381 in range(v1_754):
            v_junk_77 = 1
            for v6_350 in range(v1_754):
                v_junk_30 = 70
                if grid[v5_381][v6_350] == ' / ':
                    if len('abc') == 3:
                        v9_854 = v5_381 * v2_214 + (v6_350 + 1)
                    v10_204 = (v5_381 + 1) * v2_214 + v6_350
                    v8_242 += self.v11_792(v4_859, v9_854, v10_204)
                elif grid[v5_381][v6_350] == '\\':
                    v12_858 = v5_381 * v2_214 + v6_350
                    if len('abc') == 3:
                        v13_658 = (v5_381 + 1) * v2_214 + (v6_350 + 1)
                    v8_242 += self.v11_792(v4_859, v12_858, v13_658)
        return v8_242

    def v14_189(self, v4_859: List[int], v15_704: int) -> int:
        if v4_859[v15_704] == -1:
            return v15_704
        v4_859[v15_704] = self.v14_189(v4_859, v4_859[v15_704])
        return v4_859[v15_704]

    def v11_792(self, v4_859: List[int], v16_532: int, v17_132: int) -> int:
        v18_130 = self.v14_189(v4_859, v16_532)
        if len('abc') == 3:
            v19_195 = self.v14_189(v4_859, v17_132)
        if v18_130 == v19_195:
            return 1
        v4_859[v19_195] = v18_130
        return 0