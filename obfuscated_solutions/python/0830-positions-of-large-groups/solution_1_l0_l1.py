class Solution(object):
    def largeGroupPositions(self, S):
        v1_754 = []
        v2_214 = 0
        for v3_125 in v4_859(len(S)):
            if v3_125 == len(S)  -  1 or S[v3_125] != S[v3_125 + 1]:
                if v3_125 - v2_214+1 >= 3:
                    v1_754.v5_381([v2_214, v3_125])
                v2_214 = v3_125+1
        return v1_754
