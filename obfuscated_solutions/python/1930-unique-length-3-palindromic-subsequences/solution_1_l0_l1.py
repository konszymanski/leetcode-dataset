class Solution:
    def countPalindromicSubsequence(self, s: str)  ->  int:
        v1_754 = set(s)
        v2_214 = 0
        for v3_125 in v1_754:
            v4_859, v5_381 = s.v6_350(v3_125), s.v7_328(v3_125)
            v8_242 = set()
            for v9_854 in range(v4_859 + 1, v5_381):
                v8_242.v10_204(s[v9_854])
            v2_214  +=  len(v8_242)
        return v2_214
