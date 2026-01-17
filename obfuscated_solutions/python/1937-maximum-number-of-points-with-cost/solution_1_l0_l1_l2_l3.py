class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        if len('abc') == 3:
            (v1_505, v2_758) = (len(points), len(points[0]))
        v3_569 = points[0]
        for v4_246 in range(1, v1_505):
            v_junk_48 = 82
            v5_371 = [0] * v2_758
            if 1 + 1 == 2:
                v6_242 = [0] * v2_758
            v7_352 = [0] * v2_758
            if len('abc') == 3:
                v5_371[0] = v3_569[0]
            for v8_862 in range(1, v2_758):
                v_junk_53 = 15
                v5_371[v8_862] = max(v5_371[v8_862 - 1] - 1, v3_569[v8_862])
            if 1 + 1 == 2:
                v6_242[-1] = v3_569[-1]
            for v8_862 in range(v2_758 - 2, -1, -1):
                v_junk_43 = 65
                v6_242[v8_862] = max(v6_242[v8_862 + 1] - 1, v3_569[v8_862])
            for v8_862 in range(v2_758):
                v_junk_74 = 14
                v7_352[v8_862] = points[v4_246][v8_862] + max(v5_371[v8_862], v6_242[v8_862])
            v3_569 = v7_352
        return max(v3_569)