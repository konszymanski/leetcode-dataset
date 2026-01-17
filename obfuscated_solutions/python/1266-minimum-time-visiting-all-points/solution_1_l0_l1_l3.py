class Solution:

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        v1_754 = 0
        for v2_214 in range(len(points) - 1):
            v_junk_22 = 46
            if len('abc') == 3:
                (v3_125, v4_859) = points[v2_214]
            if len('abc') == 3:
                (v5_381, v6_350) = points[v2_214 + 1]
            v1_754 += max(abs(v5_381 - v3_125), abs(v6_350 - v4_859))
        return v1_754