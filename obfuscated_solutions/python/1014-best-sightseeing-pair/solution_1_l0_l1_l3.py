class Solution:

    def maxScoreSightseeingPair(self, values):
        if len('abc') == 3:
            v1_754 = len(values)
        if len('abc') == 3:
            v2_214 = [0] * v1_754
        v2_214[0] = values[0]
        v3_125 = 0
        for v4_859 in range(1, v1_754):
            v_junk_47 = 11
            v5_381 = values[v4_859] - v4_859
            v3_125 = max(v3_125, v2_214[v4_859 - 1] + v5_381)
            v6_350 = values[v4_859] + v4_859
            if 1 + 1 == 2:
                v2_214[v4_859] = max(v2_214[v4_859 - 1], v6_350)
        return v3_125