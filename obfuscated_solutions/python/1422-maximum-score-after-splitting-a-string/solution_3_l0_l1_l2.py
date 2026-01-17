class Solution:

    def maxScore(self, s: str) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = -v4_859
        for v5_381 in range(len(s) - 1):
            if s[v5_381] != '1':
                v2_214 = v2_214 + 1
            else:
                v1_754 = v1_754 + 1
            v3_125 = max(v3_125, v2_214 - v1_754)
        if s[-1] == '1':
            v1_754 = v1_754 + 1
        return v3_125 + v1_754