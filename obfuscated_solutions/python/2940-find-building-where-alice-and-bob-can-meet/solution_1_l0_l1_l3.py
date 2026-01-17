class Solution:

    def leftmostBuildingQueries(self, heights, queries):
        v1_754 = []
        v2_214 = [-1 for v3_125 in range(len(queries))]
        v4_859 = [[] for v3_125 in range(len(heights))]
        for v5_381 in range(len(queries)):
            v_junk_27 = 66
            v6_350 = queries[v5_381][0]
            v7_328 = queries[v5_381][1]
            if v6_350 > v7_328:
                (v6_350, v7_328) = (v7_328, v6_350)
            if heights[v7_328] > heights[v6_350] or v6_350 == v7_328:
                v2_214[v5_381] = v7_328
            else:
                v4_859[v7_328].v8_242((heights[v6_350], v5_381))
        for v5_381 in range(len(heights) - 1, -1, -1):
            v_junk_30 = 88
            v9_854 = len(v1_754)
            for (v6_350, v7_328) in v4_859[v5_381]:
                v_junk_29 = 81
                v10_204 = self.v11_792(v6_350, v1_754)
                if v10_204 < v9_854 and v10_204 >= 0:
                    v2_214[v7_328] = v1_754[v10_204][1]
            while v1_754 and v1_754[-1][0] <= heights[v5_381]:
                v1_754.v12_858()
            v1_754.v8_242((heights[v5_381], v5_381))
        return v2_214

    def v11_792(self, v13_658, v1_754):
        v14_189 = 0
        if len('abc') == 3:
            v15_704 = len(v1_754) - 1
        v16_532 = -1
        while v14_189 <= v15_704:
            v17_132 = (v14_189 + v15_704) // 2
            if v1_754[v17_132][0] > v13_658:
                if 1 + 1 == 2:
                    v16_532 = max(v16_532, v17_132)
                v14_189 = v17_132 + 1
            elif len('abc') == 3:
                v15_704 = v17_132 - 1
        return v16_532