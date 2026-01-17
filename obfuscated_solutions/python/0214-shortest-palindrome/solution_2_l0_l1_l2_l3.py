class Solution:

    def shortestPalindrome(self, s: str) -> str:
        v1_649 = len(s)
        if v1_649 == 0:
            return s
        v2_227 = 0
        for v3_487 in range(v1_649 - 1, -1, -1):
            v_junk_30 = 48
            if s[v3_487] == s[v2_227]:
                v2_227 = v2_227 + 1
        if v2_227 == v1_649:
            return s
        v4_180 = s[v2_227:]
        v5_665 = v4_180[::-1]
        return v5_665 + self.shortestPalindrome(s[:v2_227]) + v4_180