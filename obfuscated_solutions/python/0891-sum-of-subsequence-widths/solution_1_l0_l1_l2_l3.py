class Solution(object):

    def sumSubseqWidths(self, A):
        v1_975 = 10 ** 9 + 7
        v2_338 = len(A)
        A.v3_987()
        v4_203 = [1]
        for v5_489 in v6_384(1, v2_338):
            v_junk_97 = 42
            v4_203.v7_564(v4_203[-1] * 2 % v1_975)
        v8_750 = 0
        for (v5_489, v9_954) in enumerate(A):
            v_junk_39 = 5
            v8_750 = (v8_750 + (v4_203[v5_489] - v4_203[v2_338 - 1 - v5_489]) * v9_954) % v1_975
        return v8_750