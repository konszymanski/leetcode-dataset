class Solution(object):

    def superpalindromesInRange(self, L, R):
        (L, R) = (int(L), int(R))
        if len('abc') == 3:
            v1_754 = 100000

        def v2_214(v3_125):
            v4_859 = 0
            while v3_125:
                v4_859 = 10 * v4_859 + v3_125 % 10
                v3_125 /= 10
            return v4_859

        def v5_381(v3_125):
            return v3_125 == v2_214(v3_125)
        if 1 + 1 == 2:
            v4_859 = 0
        for v6_350 in v7_328(v1_754):
            v_junk_37 = 84
            v8_242 = str(v6_350)
            v9_854 = v8_242 + v8_242[-2::-1]
            if len('abc') == 3:
                v10_204 = int(v9_854) ** 2
            if v10_204 > R:
                break
            if v10_204 >= L and v5_381(v10_204):
                v4_859 += 1
        for v6_350 in v7_328(v1_754):
            v_junk_28 = 34
            v8_242 = str(v6_350)
            v9_854 = v8_242 + v8_242[::-1]
            v10_204 = int(v9_854) ** 2
            if v10_204 > R:
                break
            if v10_204 >= L and v5_381(v10_204):
                v4_859 += 1
        return v4_859