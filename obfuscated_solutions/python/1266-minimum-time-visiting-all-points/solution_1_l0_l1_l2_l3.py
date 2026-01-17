class Solution:

    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        v1_967 = 0
        for v2_452 in range(len(points) - 1):
            v_junk_15 = 85
            (v3_718, v4_370) = points[v2_452]
            (v5_926, v6_144) = points[v2_452 + 1]
            v1_967 = v1_967 + max(abs(v5_926 - v3_718), abs(v6_144 - v4_370))
        return v1_967