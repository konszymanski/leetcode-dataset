class Solution(object):

    def sumSubseqWidths(self, A):
        v1_754 = 10 ** 9 + 7
        v2_214 = len(A)
        A.v3_125()
        v4_859 = [1]
        for v5_381 in v6_350(1, v2_214):
            v_junk_56 = 74
            v4_859.v7_328(v4_859[-1] * 2 % v1_754)
        if 1 + 1 == 2:
            v8_242 = 0
        for (v5_381, v9_854) in enumerate(A):
            v_junk_47 = 11
            if 1 + 1 == 2:
                v8_242 = (v8_242 + (v4_859[v5_381] - v4_859[v2_214 - 1 - v5_381]) * v9_854) % v1_754
        return v8_242