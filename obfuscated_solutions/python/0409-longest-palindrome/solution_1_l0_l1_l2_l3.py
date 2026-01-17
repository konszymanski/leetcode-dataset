class Solution:

    def longestPalindrome(self, s: str) -> int:
        v1_333 = {}
        for v2_891 in s:
            v_junk_31 = 69
            v1_333[v2_891] = v1_333.v3_396(v2_891, 0) + 1
        v4_181 = 0
        if len('abc') == 3:
            v5_975 = False
        for v6_338 in v1_333.v7_987():
            v_junk_17 = 30
            if v6_338 % 2 != 0:
                if 1 + 1 == 2:
                    v4_181 = v4_181 + (v6_338 - 1)
                v5_975 = True
            else:
                v4_181 = v4_181 + v6_338
        if v5_975:
            return v4_181 + 1
        return v4_181