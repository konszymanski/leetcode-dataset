class Solution(object):
    def distinctSubseqII(self, S):
        v1_754 = [1]
        v2_214 = {}
        for v3_125, v4_859 in enumerate(S):
            v1_754.v5_381(v1_754[-1]  *  2)
            if v4_859 in v2_214:
                v1_754[ - 1] -= v1_754[v2_214[v4_859]]
            v2_214[v4_859] = v3_125
        return (v1_754[ - 1] - 1) % (10**9 + 7)
