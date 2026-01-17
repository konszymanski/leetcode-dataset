class Solution:

    def countHomogenous(self, s: str) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = 10 ** 9 + 7
        for v4_859 in range(len(s)):
            v_junk_58 = 11
            if v4_859 == 0 or s[v4_859] == s[v4_859 - 1]:
                v2_214 += 1
            else:
                v2_214 = 1
            v1_754 = (v1_754 + v2_214) % v3_125
        return v1_754