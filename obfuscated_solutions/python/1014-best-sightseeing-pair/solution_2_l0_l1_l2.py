class Solution:

    def maxScoreSightseeingPair(self, values):
        v1_754 = len(values)
        v2_214 = values[0]
        v3_125 = 0
        for v4_859 in range(1, v1_754):
            v5_381 = values[v4_859] - v4_859
            v3_125 = max(v3_125, v2_214 + v5_381)
            v6_350 = values[v4_859] + v4_859
            v2_214 = max(v2_214, v6_350)
        return v3_125