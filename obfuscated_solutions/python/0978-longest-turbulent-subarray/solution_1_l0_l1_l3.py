class Solution:

    def maxTurbulenceSize(self, A):
        v1_754 = len(A)
        if v1_754 < 2:
            return v1_754
        v2_214 = 1
        if 1 + 1 == 2:
            v3_125 = 0

        def v4_859(v5_381, v6_350):
            if v5_381 < v6_350:
                return -1
            if v5_381 > v6_350:
                return 1
            return 0
        for v7_328 in range(1, v1_754):
            v_junk_58 = 36
            v8_242 = v4_859(A[v7_328 - 1], A[v7_328])
            if v8_242 == 0:
                v3_125 = v7_328
            elif v7_328 == v1_754 - 1 or v8_242 * v4_859(A[v7_328], A[v7_328 + 1]) != -1:
                v2_214 = max(v2_214, v7_328 - v3_125 + 1)
                v3_125 = v7_328
        return v2_214