class Solution:

    def leftmostBuildingQueries(self, heights, queries):
        v1_754 = []
        v2_214 = [-1] * len(queries)
        v3_125 = [[] for v4_859 in heights]
        for (v5_381, v6_350) in enumerate(queries):
            (v7_328, v8_242) = v6_350
            if v7_328 < v8_242 and heights[v7_328] < heights[v8_242]:
                v2_214[v5_381] = v8_242
            elif v7_328 > v8_242 and heights[v7_328] > heights[v8_242]:
                v2_214[v5_381] = v7_328
            elif v7_328 != v8_242:
                v3_125[max(v7_328, v8_242)].v9_854((max(heights[v7_328], heights[v8_242]), v5_381))
            else:
                v2_214[v5_381] = v7_328
        for (v5_381, v10_204) in enumerate(heights):
            while v1_754 and v1_754[0][0] < v10_204:
                (v4_859, v11_792) = v12_858.v13_658(v1_754)
                v2_214[v11_792] = v5_381
            for v14_189 in v3_125[v5_381]:
                v12_858.v15_704(v1_754, v14_189)
        return v2_214