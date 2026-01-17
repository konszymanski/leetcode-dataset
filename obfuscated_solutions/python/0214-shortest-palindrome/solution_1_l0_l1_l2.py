class Solution:

    def shortestPalindrome(self, s: str) -> str:
        v1_754 = len(s)
        v2_214 = s[::-1]
        for v3_125 in range(v1_754):
            if s[:v1_754 - v3_125] == v2_214[v3_125:]:
                return v2_214[:v3_125] + s
        return ''