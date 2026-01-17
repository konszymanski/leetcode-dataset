class Solution:

    def maxPoints(self, points: List[List[int]]) -> int:
        (v1_754, v2_214) = (len(points), len(points[0]))
        v3_125 = points[0]
        for v4_859 in range(1, v1_754):
            v5_381 = [0] * v2_214
            v6_350 = [0] * v2_214
            v7_328 = [0] * v2_214
            v5_381[0] = v3_125[0]
            for v8_242 in range(1, v2_214):
                v5_381[v8_242] = max(v5_381[v8_242 - 1] - 1, v3_125[v8_242])
            v6_350[-1] = v3_125[-1]
            for v8_242 in range(v2_214 - 2, -1, -1):
                v6_350[v8_242] = max(v6_350[v8_242 + 1] - 1, v3_125[v8_242])
            for v8_242 in range(v2_214):
                v7_328[v8_242] = points[v4_859][v8_242] + max(v5_381[v8_242], v6_350[v8_242])
            v3_125 = v7_328
        return max(v3_125)