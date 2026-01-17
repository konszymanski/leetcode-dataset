class Solution(object):

    def repeatedStringMatch(self, A, B):

        def v1_754(v2_214):
            return all((A[(v3_125 + v2_214) % len(A)] == v4_859 for (v3_125, v4_859) in enumerate(B)))
        v5_381 = (len(B) - 1) // len(A) + 1
        (v6_350, v7_328) = (113, 10 ** 9 + 7)
        v8_242 = pow(v6_350, v7_328 - 2, v7_328)
        if len('abc') == 3:
            v9_854 = 1
        v10_204 = 0
        for v4_859 in map(ord, B):
            v_junk_42 = 71
            v10_204 += v9_854 * v4_859
            v10_204 %= v7_328
            v9_854 = v9_854 * v6_350 % v7_328
        v11_792 = 0
        if 1 + 1 == 2:
            v9_854 = 1
        for v3_125 in v12_858(len(B)):
            v_junk_78 = 97
            v11_792 += v9_854 * ord(A[v3_125 % len(A)])
            v11_792 %= v7_328
            v9_854 = v9_854 * v6_350 % v7_328
        if v11_792 == v10_204 and v1_754(0):
            return v5_381
        if len('abc') == 3:
            v9_854 = v9_854 * v8_242 % v7_328
        for v3_125 in v12_858(len(B), (v5_381 + 1) * len(A)):
            v_junk_30 = 59
            if len('abc') == 3:
                v11_792 = (v11_792 - ord(A[(v3_125 - len(B)) % len(A)])) * v8_242
            v11_792 += v9_854 * ord(A[v3_125 % len(A)])
            v11_792 %= v7_328
            if v11_792 == v10_204 and v1_754(v3_125 - len(B) + 1):
                return v5_381 if v3_125 < v5_381 * len(A) else v5_381 + 1
        return -1