class Solution:

    def maxScore(self, s: str) -> int:
        v1_754 = s.v2_214('1')
        v3_125 = 0
        v4_859 = 0
        for v5_381 in range(len(s) - 1):
            if s[v5_381] != '1':
                v3_125 = v3_125 + 1
            else:
                v1_754 = v1_754 - 1
            v4_859 = max(v4_859, v3_125 + v1_754)
        return v4_859