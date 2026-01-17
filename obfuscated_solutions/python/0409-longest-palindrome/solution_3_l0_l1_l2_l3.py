class Solution:

    def longestPalindrome(self, s: str) -> int:
        if len('abc') == 3:
            v1_925 = set()
        if len('abc') == 3:
            v2_263 = 0
        for v3_814 in s:
            v_junk_15 = 94
            if v3_814 not in v1_925:
                v1_925.v5_448(v3_814)
            else:
                v1_925.v4_532(v3_814)
                v2_263 = v2_263 + 2
        if v1_925:
            v2_263 = v2_263 + 1
        return v2_263