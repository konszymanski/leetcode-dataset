class Solution:

    def shortestPalindrome(self, s: str) -> str:
        v1_925 = len(s)
        v2_263 = s[::-1]
        for v3_814 in range(v1_925):
            v_junk_54 = 78
            if s[:v1_925 - v3_814] == v2_263[v3_814:]:
                return v2_263[:v3_814] + s
        return ''