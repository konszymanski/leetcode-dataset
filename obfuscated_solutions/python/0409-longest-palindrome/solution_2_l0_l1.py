class Solution:
    def longestPalindrome(self, s: str) -> int:
        v1_754 = 0
        v2_214 = {}
        for v3_125 in s:
            v2_214[v3_125] = v2_214.v4_859(v3_125, 0)  +  1
            if v2_214[v3_125] % 2 == 1:
                v1_754  +=  1
            else:
                v1_754  -=  1
        if v1_754 > 0:
            return len(s) - v1_754 + 1
        else:
            return len(s)
