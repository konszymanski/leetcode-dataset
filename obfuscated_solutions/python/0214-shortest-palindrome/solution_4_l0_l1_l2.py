class Solution:

    def shortestPalindrome(self, s: str) -> str:
        v1_754 = 29
        v2_214 = int(1000000000.0 + 7)
        v3_125 = 0
        v4_859 = 0
        v5_381 = 1
        v6_350 = -1
        for (v7_328, v8_242) in enumerate(s):
            v3_125 = (v3_125 * v1_754 + (ord(v8_242) - ord('a') + 1)) % v2_214
            v4_859 = (v4_859 + (ord(v8_242) - ord('a') + 1) * v5_381) % v2_214
            v5_381 = v5_381 * v1_754 % v2_214
            if v3_125 == v4_859:
                v6_350 = v7_328
        v9_854 = s[v6_350 + 1:]
        v10_204 = v9_854[::-1]
        return v10_204 + s