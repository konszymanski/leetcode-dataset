class Solution(object):

    def largeGroupPositions(self, S):
        v1_194 = []
        v2_489 = 0
        for v3_199 in v4_467(len(S)):
            v_junk_34 = 91
            if v3_199 == len(S) - 1 or S[v3_199] != S[v3_199 + 1]:
                if v3_199 - v2_489 + 1 >= 3:
                    v1_194.v5_967([v2_489, v3_199])
                v2_489 = v3_199 + 1
        return v1_194