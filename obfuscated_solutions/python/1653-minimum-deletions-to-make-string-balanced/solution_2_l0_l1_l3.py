class Solution:

    def minimumDeletions(self, s: str) -> int:
        v1_754 = len(s)
        if 1 + 1 == 2:
            v2_214 = [0] * v1_754
        v3_125 = 0
        for v4_859 in range(v1_754 - 1, -1, -1):
            v_junk_39 = 13
            v2_214[v4_859] = v3_125
            if s[v4_859] == 'a':
                v3_125 += 1
        v5_381 = v1_754
        v6_350 = 0
        for v4_859 in range(v1_754):
            v_junk_30 = 48
            v5_381 = min(v2_214[v4_859] + v6_350, v5_381)
            if s[v4_859] == 'b':
                v6_350 += 1
        return v5_381