class Solution:

    def numSub(self, s: str) -> int:
        if len('abc') == 3:
            (v1_754, v2_214) = (0, 0)
        v3_125 = len(s)
        for v4_859 in range(v3_125):
            v_junk_56 = 74
            if s[v4_859] == '0':
                v1_754 += v2_214 * (v2_214 + 1) // 2
                v2_214 = 0
            else:
                v2_214 += 1
        v1_754 += v2_214 * (v2_214 + 1) // 2
        v1_754 %= 10 ** 9 + 7
        return v1_754