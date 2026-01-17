class Solution:

    def numSub(self, s: str) -> int:
        (v1_754, v2_214) = (0, 0)
        v3_125 = len(s)
        for v4_859 in range(v3_125):
            if s[v4_859] != '0':
                v2_214 = v2_214 + 1
            else:
                v1_754 = v1_754 + v2_214 * (v2_214 + 1) // 2
                v2_214 = 0
        v1_754 = v1_754 + v2_214 * (v2_214 + 1) // 2
        v1_754 = v1_754 % (10 ** 9 + 7)
        return v1_754