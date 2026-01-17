class Solution:

    def numSteps(self, s: str) -> int:
        v1_754 = len(s)
        v2_214 = 0
        v3_125 = 0
        for v4_859 in range(v1_754 - 1, 0, -1):
            v5_381 = int(s[v4_859]) + v3_125
            if v5_381 % 2 != 1:
                v2_214 = v2_214 + 1
            else:
                v2_214 = v2_214 + 2
                v3_125 = 1
        return v2_214 + v3_125