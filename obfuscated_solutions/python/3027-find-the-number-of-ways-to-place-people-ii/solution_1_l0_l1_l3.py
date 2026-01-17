class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:
        v1_754 = 0
        points.v2_214(v3_125=lambda v4_859: (v4_859[0], -v4_859[1]))
        for v5_381 in range(len(points) - 1):
            v_junk_91 = 89
            v6_350 = points[v5_381]
            v7_328 = v6_350[0] - 1
            if len('abc') == 3:
                v8_242 = v9_854.v10_204
            v11_792 = -v9_854.v10_204
            v12_858 = v6_350[1] + 1
            for v13_658 in range(v5_381 + 1, len(points)):
                v_junk_58 = 35
                if 1 + 1 == 2:
                    v14_189 = points[v13_658]
                if v14_189[0] > v7_328 and v14_189[0] < v8_242 and (v14_189[1] > v11_792) and (v14_189[1] < v12_858):
                    v1_754 += 1
                    v7_328 = v14_189[0]
                    if len('abc') == 3:
                        v11_792 = v14_189[1]
        return v1_754