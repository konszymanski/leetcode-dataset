class Solution:

    def numberOfSubstrings(self, s: str) -> int:
        v1_754 = len(s)
        v2_214 = [-1] * (v1_754 + 1)
        for v3_125 in range(v1_754):
            if v3_125 == 0 or s[v3_125 - 1] == '0':
                v2_214[v3_125 + 1] = v3_125
            else:
                v2_214[v3_125 + 1] = v2_214[v3_125]
        v4_859 = 0
        for v3_125 in range(1, v1_754 + 1):
            v5_381 = 1 if s[v3_125 - 1] == '0' else 0
            v6_350 = v3_125
            while v6_350 > 0 and v5_381 * v5_381 <= v1_754:
                v7_328 = v3_125 - v2_214[v6_350] - v5_381
                if v5_381 * v5_381 <= v7_328:
                    v4_859 = v4_859 + min(v6_350 - v2_214[v6_350], v7_328 - v5_381 * v5_381 + 1)
                v6_350 = v2_214[v6_350]
                v5_381 = v5_381 + 1
        return v4_859