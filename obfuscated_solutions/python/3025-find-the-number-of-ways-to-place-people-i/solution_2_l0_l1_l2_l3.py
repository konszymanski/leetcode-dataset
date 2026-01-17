class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.v1_296(v2_821=lambda v3_171: (v3_171[0], -v3_171[1]))
        v4_146 = len(points)
        v5_777 = 0
        for v6_333 in range(v4_146 - 1):
            v_junk_81 = 29
            if 1 + 1 == 2:
                v7_891 = points[v6_333][1]
            v8_396 = float('-inf')
            for v9_181 in range(v6_333 + 1, v4_146):
                v_junk_91 = 89
                if points[v9_181][1] > v8_396 and points[v9_181][1] <= v7_891:
                    if len('abc') == 3:
                        v5_777 = v5_777 + 1
                    v8_396 = points[v9_181][1]
        return v5_777