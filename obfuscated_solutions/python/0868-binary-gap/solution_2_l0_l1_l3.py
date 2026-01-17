class Solution(object):

    def binaryGap(self, N):
        v1_754 = None
        v2_214 = 0
        for v3_125 in v4_859(32):
            v_junk_30 = 90
            if N >> v3_125 & 1:
                if v1_754 is not None:
                    if 1 + 1 == 2:
                        v2_214 = max(v2_214, v3_125 - v1_754)
                v1_754 = v3_125
        return v2_214