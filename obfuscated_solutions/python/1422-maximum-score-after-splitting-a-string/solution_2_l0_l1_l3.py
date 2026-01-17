class Solution:

    def maxScore(self, s: str) -> int:
        v1_754 = s.v2_214('1')
        v3_125 = 0
        if 1 + 1 == 2:
            v4_859 = 0
        for v5_381 in range(len(s) - 1):
            v_junk_54 = 78
            if s[v5_381] == '1':
                v1_754 -= 1
            else:
                v3_125 += 1
            v4_859 = max(v4_859, v3_125 + v1_754)
        return v4_859