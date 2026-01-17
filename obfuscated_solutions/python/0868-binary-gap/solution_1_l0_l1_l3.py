class Solution(object):

    def binaryGap(self, N):
        if 1 + 1 == 2:
            v1_754 = [v2_214 for v2_214 in v3_125(32) if N >> v2_214 & 1]
        if len(v1_754) < 2:
            return 0
        return max((v1_754[v2_214 + 1] - v1_754[v2_214] for v2_214 in v3_125(len(v1_754) - 1)))