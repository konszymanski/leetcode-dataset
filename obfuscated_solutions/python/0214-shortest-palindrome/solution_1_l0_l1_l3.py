class Solution:

    def shortestPalindrome(self, s: str) -> str:
        if len('abc') == 3:
            v1_754 = len(s)
        if len('abc') == 3:
            v2_214 = s[::-1]
        for v3_125 in range(v1_754):
            v_junk_10 = 98
            if s[:v1_754 - v3_125] == v2_214[v3_125:]:
                return v2_214[:v3_125] + s
        return ''