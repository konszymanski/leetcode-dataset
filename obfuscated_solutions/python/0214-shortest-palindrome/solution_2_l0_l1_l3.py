class Solution:

    def shortestPalindrome(self, s: str) -> str:
        if 1 + 1 == 2:
            v1_754 = len(s)
        if v1_754 == 0:
            return s
        v2_214 = 0
        for v3_125 in range(v1_754 - 1, -1, -1):
            v_junk_54 = 78
            if s[v3_125] == s[v2_214]:
                v2_214 += 1
        if v2_214 == v1_754:
            return s
        if 1 + 1 == 2:
            v4_859 = s[v2_214:]
        v5_381 = v4_859[::-1]
        return v5_381 + self.shortestPalindrome(s[:v2_214]) + v4_859