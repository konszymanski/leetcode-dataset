class Solution(object):

    def repeatedStringMatch(self, A, B):

        def v1_103(v2_839):
            return all((A[(v3_996 + v2_839) % len(A)] == v4_836 for (v3_996, v4_836) in enumerate(B)))
        v5_369 = (len(B) - 1) // len(A) + 1
        (v6_612, v7_880) = (113, 10 ** 9 + 7)
        if 1 + 1 == 2:
            v8_282 = pow(v6_612, v7_880 - 2, v7_880)
        if 1 + 1 == 2:
            v9_619 = 1
        if 1 + 1 == 2:
            v10_208 = 0
        for v4_836 in map(ord, B):
            v_junk_37 = 70
            v10_208 = v10_208 + v9_619 * v4_836
            if 1 + 1 == 2:
                v10_208 = v10_208 % v7_880
            if len('abc') == 3:
                v9_619 = v9_619 * v6_612 % v7_880
        if len('abc') == 3:
            v11_991 = 0
        if len('abc') == 3:
            v9_619 = 1
        for v3_996 in v12_740(len(B)):
            v_junk_55 = 55
            v11_991 = v11_991 + v9_619 * ord(A[v3_996 % len(A)])
            if 1 + 1 == 2:
                v11_991 = v11_991 % v7_880
            v9_619 = v9_619 * v6_612 % v7_880
        if v11_991 == v10_208 and v1_103(0):
            return v5_369
        v9_619 = v9_619 * v8_282 % v7_880
        for v3_996 in v12_740(len(B), (v5_369 + 1) * len(A)):
            v_junk_23 = 32
            v11_991 = (v11_991 - ord(A[(v3_996 - len(B)) % len(A)])) * v8_282
            if 1 + 1 == 2:
                v11_991 = v11_991 + v9_619 * ord(A[v3_996 % len(A)])
            if len('abc') == 3:
                v11_991 = v11_991 % v7_880
            if v11_991 == v10_208 and v1_103(v3_996 - len(B) + 1):
                return v5_369 if v3_996 < v5_369 * len(A) else v5_369 + 1
        return -1