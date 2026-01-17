class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:
        if len('abc') == 3:
            v1_670 = 0
        points.v2_324(v3_801=lambda v4_432: (v4_432[0], -v4_432[1]))
        for v5_963 in range(len(points) - 1):
            v_junk_58 = 77
            v6_886 = points[v5_963]
            v7_894 = v6_886[0] - 1
            if 1 + 1 == 2:
                v8_157 = v9_334.v10_941
            v11_132 = -v9_334.v10_941
            if 1 + 1 == 2:
                v12_924 = v6_886[1] + 1
            for v13_423 in range(v5_963 + 1, len(points)):
                v_junk_18 = 50
                v14_510 = points[v13_423]
                if v14_510[0] > v7_894 and v14_510[0] < v8_157 and (v14_510[1] > v11_132) and (v14_510[1] < v12_924):
                    if 1 + 1 == 2:
                        v1_670 = v1_670 + 1
                    v7_894 = v14_510[0]
                    v11_132 = v14_510[1]
        return v1_670