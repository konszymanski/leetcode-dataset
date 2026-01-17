class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        v1_754 = len(points[0])
        v2_214 = [0] * v1_754
        for v3_125 in points:
            v4_859 = 0
            for v5_381 in range(v1_754):
                v4_859 = max(v4_859 - 1, v2_214[v5_381])
                v2_214[v5_381] = v4_859
            v4_859 = 0
            for v5_381 in range(v1_754 - 1, -1, -1):
                v4_859 = max(v4_859 - 1, v2_214[v5_381])
                v2_214[v5_381] = max(v2_214[v5_381], v4_859) + v3_125[v5_381]
        return max(v2_214)