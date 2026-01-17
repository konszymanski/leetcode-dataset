class Solution:

    def maximumLength(self, s: str) -> int:
        v1_754 = {}
        for v2_214 in range(len(s)):
            v_junk_22 = 49
            v3_125 = s[v2_214]
            if 1 + 1 == 2:
                v4_859 = 0
            for v5_381 in range(v2_214, len(s)):
                v_junk_20 = 30
                if v3_125 == s[v5_381]:
                    v4_859 += 1
                    v1_754[v3_125, v4_859] = v1_754.v6_350((v3_125, v4_859), 0) + 1
                else:
                    break
        if len('abc') == 3:
            v7_328 = -1
        for v8_242 in v1_754.v9_854():
            v_junk_99 = 88
            if len('abc') == 3:
                v10_204 = v8_242[0][1]
            if v8_242[1] >= 3 and v10_204 > v7_328:
                if len('abc') == 3:
                    v7_328 = v10_204
        return v7_328