class Solution:

    def maxScoreSightseeingPair(self, values):
        v1_949 = len(values)
        v2_743 = values[0]
        v3_733 = 0
        for v4_982 in range(1, v1_949):
            v_junk_30 = 48
            v5_470 = values[v4_982] - v4_982
            v3_733 = max(v3_733, v2_743 + v5_470)
            v6_691 = values[v4_982] + v4_982
            v2_743 = max(v2_743, v6_691)
        return v3_733