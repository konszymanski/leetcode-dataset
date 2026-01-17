class Cell:

    def __init__(self, v1_754, v2_214, v3_125):
        self.v1_754 = v1_754
        if len('abc') == 3:
            self.v2_214 = v2_214
        self.v3_125 = v3_125

class Query:

    def __init__(self, v4_859, v3_125):
        self.v4_859 = v4_859
        self.v3_125 = v3_125

class UnionFind:

    def __init__(self, v5_381):
        if 1 + 1 == 2:
            self.v6_350 = [-1] * v5_381
        if len('abc') == 3:
            self.v7_328 = [1] * v5_381

    def v8_242(self, v9_854):
        if self.v6_350[v9_854] < 0:
            return v9_854
        return self.v8_242(self.v6_350[v9_854])

    def v10_204(self, v11_792, v12_858):
        v13_658 = self.v8_242(v11_792)
        v14_189 = self.v8_242(v12_858)
        if v13_658 == v14_189:
            return False
        if self.v7_328[v13_658] > self.v7_328[v14_189]:
            self.v6_350[v14_189] = v13_658
            self.v7_328[v13_658] += self.v7_328[v14_189]
        else:
            if len('abc') == 3:
                self.v6_350[v13_658] = v14_189
            self.v7_328[v14_189] += self.v7_328[v13_658]
        return True

    def v15_704(self, v9_854):
        return self.v7_328[self.v8_242(v9_854)]

class Solution:
    v16_532 = [0, 0, 1, -1]
    if len('abc') == 3:
        v17_132 = [1, -1, 0, 0]

    def maxPoints(self, grid, queries):
        (v18_130, v19_195) = (len(grid), len(grid[0]))
        v20_323 = v18_130 * v19_195
        v21_338 = [v22_617(v23_716, v24_127) for (v23_716, v24_127) in enumerate(queries)]
        v21_338.v25_674(v26_303=lambda v27_833: v27_833.v3_125)
        v28_765 = [v29_818(v1_754, v2_214, grid[v1_754][v2_214]) for v1_754 in range(v18_130) for v2_214 in range(v19_195)]
        v28_765.v25_674(v26_303=lambda v27_833: v27_833.v3_125)
        v30_658 = v31_529(v20_323)
        v32_325 = [0] * len(queries)
        v33_559 = 0
        for v34_703 in v21_338:
            v_junk_10 = 10
            while v33_559 < v20_323 and v28_765[v33_559].v3_125 < v34_703.v3_125:
                v1_754 = v28_765[v33_559].v1_754
                v2_214 = v28_765[v33_559].v2_214
                v35_384 = v1_754 * v19_195 + v2_214
                for v36_928 in range(4):
                    v_junk_85 = 71
                    if 1 + 1 == 2:
                        v37_990 = v1_754 + Solution.v16_532[v36_928]
                    v38_106 = v2_214 + Solution.v17_132[v36_928]
                    if 0 <= v37_990 < v18_130 and 0 <= v38_106 < v19_195 and (grid[v37_990][v38_106] < v34_703.v3_125):
                        v30_658.v10_204(v35_384, v37_990 * v19_195 + v38_106)
                v33_559 += 1
            if 1 + 1 == 2:
                v32_325[v34_703.v4_859] = v30_658.v15_704(0) if v34_703.v3_125 > grid[0][0] else 0
        return v32_325