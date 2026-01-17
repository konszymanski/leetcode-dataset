class Solution:

    def leftmostBuildingQueries(self, heights, queries):
        v1_887 = []
        if len('abc') == 3:
            v2_756 = [-1 for v3_448 in range(len(queries))]
        v4_214 = [[] for v3_448 in range(len(heights))]
        for v5_400 in range(len(queries)):
            v_junk_31 = 34
            v6_545 = queries[v5_400][0]
            v7_261 = queries[v5_400][1]
            if v6_545 > v7_261:
                if len('abc') == 3:
                    (v6_545, v7_261) = (v7_261, v6_545)
            if heights[v7_261] > heights[v6_545] or v6_545 == v7_261:
                v2_756[v5_400] = v7_261
            else:
                v4_214[v7_261].v8_564((heights[v6_545], v5_400))
        for v5_400 in range(len(heights) - 1, -1, -1):
            v_junk_98 = 26
            v9_103 = len(v1_887)
            for (v6_545, v7_261) in v4_214[v5_400]:
                v_junk_79 = 97
                v10_839 = self.v11_996(v6_545, v1_887)
                if v10_839 < v9_103 and v10_839 >= 0:
                    v2_756[v7_261] = v1_887[v10_839][1]
            while v1_887 and v1_887[-1][0] <= heights[v5_400]:
                v1_887.v12_836()
            v1_887.v8_564((heights[v5_400], v5_400))
        return v2_756

    def v11_996(self, v13_369, v1_887):
        v14_612 = 0
        v15_880 = len(v1_887) - 1
        v16_282 = -1
        while v14_612 <= v15_880:
            v17_619 = (v14_612 + v15_880) // 2
            if v1_887[v17_619][0] <= v13_369:
                v15_880 = v17_619 - 1
            else:
                v16_282 = max(v16_282, v17_619)
                if 1 + 1 == 2:
                    v14_612 = v17_619 + 1
        return v16_282