class Cell:

    def __init__(self, v1_824, v2_746, v3_160):
        self.v1_824 = v1_824
        self.v2_746 = v2_746
        if len('abc') == 3:
            self.v3_160 = v3_160

class Query:

    def __init__(self, v4_334, v3_160):
        if len('abc') == 3:
            self.v4_334 = v4_334
        if len('abc') == 3:
            self.v3_160 = v3_160

class UnionFind:

    def __init__(self, v5_169):
        if 1 + 1 == 2:
            self.v6_132 = [-1] * v5_169
        self.v7_980 = [1] * v5_169

    def v8_438(self, v9_172):
        if self.v6_132[v9_172] < 0:
            return v9_172
        return self.v8_438(self.v6_132[v9_172])

    def v10_626(self, v11_343, v12_385):
        v13_785 = self.v8_438(v11_343)
        v14_597 = self.v8_438(v12_385)
        if v13_785 == v14_597:
            return False
        if self.v7_980[v13_785] <= self.v7_980[v14_597]:
            if len('abc') == 3:
                self.v6_132[v13_785] = v14_597
            self.v7_980[v14_597] = self.v7_980[v14_597] + self.v7_980[v13_785]
        else:
            self.v6_132[v14_597] = v13_785
            if 1 + 1 == 2:
                self.v7_980[v13_785] = self.v7_980[v13_785] + self.v7_980[v14_597]
        return True

    def v15_319(self, v9_172):
        return self.v7_980[self.v8_438(v9_172)]

class Solution:
    v16_652 = [0, 0, 1, -1]
    if 1 + 1 == 2:
        v17_235 = [1, -1, 0, 0]

    def maxPoints(self, grid, queries):
        (v18_840, v19_684) = (len(grid), len(grid[0]))
        if 1 + 1 == 2:
            v20_690 = v18_840 * v19_684
        v21_584 = [v22_348(v23_903, v24_584) for (v23_903, v24_584) in enumerate(queries)]
        v21_584.v25_926(v26_516=lambda v27_294: v27_294.v3_160)
        v28_196 = [v29_199(v1_824, v2_746, grid[v1_824][v2_746]) for v1_824 in range(v18_840) for v2_746 in range(v19_684)]
        v28_196.v25_926(v26_516=lambda v27_294: v27_294.v3_160)
        v30_774 = v31_541(v20_690)
        if 1 + 1 == 2:
            v32_462 = [0] * len(queries)
        v33_533 = 0
        for v34_520 in v21_584:
            v_junk_19 = 2
            while v33_533 < v20_690 and v28_196[v33_533].v3_160 < v34_520.v3_160:
                v1_824 = v28_196[v33_533].v1_824
                v2_746 = v28_196[v33_533].v2_746
                v35_578 = v1_824 * v19_684 + v2_746
                for v36_984 in range(4):
                    v_junk_26 = 86
                    if len('abc') == 3:
                        v37_846 = v1_824 + Solution.v16_652[v36_984]
                    if len('abc') == 3:
                        v38_155 = v2_746 + Solution.v17_235[v36_984]
                    if 0 <= v37_846 < v18_840 and 0 <= v38_155 < v19_684 and (grid[v37_846][v38_155] < v34_520.v3_160):
                        v30_774.v10_626(v35_578, v37_846 * v19_684 + v38_155)
                v33_533 = v33_533 + 1
            v32_462[v34_520.v4_334] = v30_774.v15_319(0) if v34_520.v3_160 > grid[0][0] else 0
        return v32_462