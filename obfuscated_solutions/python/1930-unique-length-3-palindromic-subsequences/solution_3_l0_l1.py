class Solution:
    def countPalindromicSubsequence(self, s: str)  ->  int:
        v1_754 = [-1] * 26
        v2_214 = [-1]  *  26
        for v3_125 in range(len(s)):
            v4_859 = ord(s[v3_125]) - ord("a")
            if v1_754[v4_859]  ==  -1:
                v1_754[v4_859] = v3_125
            v2_214[v4_859] = v3_125
        v5_381 = 0
        for v3_125 in range(26):
            if v1_754[v3_125]  ==   - 1:
                continue
            v6_350 = set()
            for v7_328 in range(v1_754[v3_125]  +  1, v2_214[v3_125]):
                v6_350.v8_242(s[v7_328])
            v5_381 += len(v6_350)
        return v5_381
