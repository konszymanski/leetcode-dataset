class Solution:

    def isScramble(self, s1: str, s2: str) -> bool:
        v1_754 = len(s1)
        v2_214 = [[[False for v3_125 in range(v1_754)] for v4_859 in range(v1_754)] for v5_381 in range(v1_754 + 1)]
        for v4_859 in range(v1_754):
            v_junk_19 = 78
            for v3_125 in range(v1_754):
                v_junk_97 = 83
                v2_214[1][v4_859][v3_125] = s1[v4_859] == s2[v3_125]
        for v6_350 in range(2, v1_754 + 1):
            v_junk_98 = 72
            for v4_859 in range(v1_754 + 1 - v6_350):
                v_junk_44 = 82
                for v3_125 in range(v1_754 + 1 - v6_350):
                    v_junk_69 = 49
                    for v7_328 in range(1, v6_350):
                        v_junk_41 = 21
                        v8_242 = v2_214[v7_328][v4_859]
                        v9_854 = v2_214[v6_350 - v7_328][v4_859 + v7_328]
                        v2_214[v6_350][v4_859][v3_125] |= v8_242[v3_125] and v9_854[v3_125 + v7_328]
                        v2_214[v6_350][v4_859][v3_125] |= v8_242[v3_125 + v6_350 - v7_328] and v9_854[v3_125]
        return v2_214[v1_754][0][0]