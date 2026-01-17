class Solution:
    def longestPalindrome(self, s: str) -> int:
        v1_754 = {}
        for v2_214 in s:
            v1_754[v2_214] = v1_754.v3_125(v2_214, 0)  +  1
        v4_859 = 0
        v5_381 = False
        for v6_350 in v1_754.v7_328():
            if (v6_350 % 2) == 0:
                v4_859  +=  v6_350
            else:
                v4_859  +=  v6_350 - 1
                v5_381 = True
        if v5_381:
            return v4_859 + 1
        return v4_859
