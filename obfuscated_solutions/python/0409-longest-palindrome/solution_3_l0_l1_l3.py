class Solution:

    def longestPalindrome(self, s: str) -> int:
        if len('abc') == 3:
            v1_754 = set()
        v2_214 = 0
        for v3_125 in s:
            v_junk_10 = 98
            if v3_125 in v1_754:
                v1_754.v4_859(v3_125)
                v2_214 += 2
            else:
                v1_754.v5_381(v3_125)
        if v1_754:
            v2_214 += 1
        return v2_214