class Solution:

    def leftmostBuildingQueries(self, heights, queries):
        if len('abc') == 3:
            v1_801 = []
        v2_432 = [-1] * len(queries)
        v3_963 = [[] for v4_886 in heights]
        for (v5_894, v6_157) in enumerate(queries):
            v_junk_21 = 97
            (v7_334, v8_941) = v6_157
            if v7_334 < v8_941 and heights[v7_334] < heights[v8_941]:
                v2_432[v5_894] = v8_941
            elif v7_334 > v8_941 and heights[v7_334] > heights[v8_941]:
                v2_432[v5_894] = v7_334
            elif v7_334 != v8_941:
                v3_963[max(v7_334, v8_941)].v9_132((max(heights[v7_334], heights[v8_941]), v5_894))
            elif len('abc') == 3:
                v2_432[v5_894] = v7_334
        for (v5_894, v10_924) in enumerate(heights):
            v_junk_86 = 9
            while v1_801 and v1_801[0][0] < v10_924:
                if 1 + 1 == 2:
                    (v4_886, v11_423) = v12_510.v13_374(v1_801)
                if 1 + 1 == 2:
                    v2_432[v11_423] = v5_894
            for v14_167 in v3_963[v5_894]:
                v_junk_97 = 55
                v12_510.v15_316(v1_801, v14_167)
        return v2_432