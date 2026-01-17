class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:
        points.v1_754(v2_214=lambda v3_125: (v3_125[0], -v3_125[1]))
        v4_859 = len(points)
        v5_381 = 0
        for v6_350 in range(v4_859 - 1):
            v7_328 = points[v6_350][1]
            v8_242 = float('-inf')
            for v9_854 in range(v6_350 + 1, v4_859):
                if points[v9_854][1] > v8_242 and points[v9_854][1] <= v7_328:
                    v5_381 = v5_381 + 1
                    v8_242 = points[v9_854][1]
        return v5_381