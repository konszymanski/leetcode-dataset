class Solution:
    def longestPalindrome(self, s: str) -> str:
        def v1_754(v2_214, v3_125):
            v4_859 = v2_214
            v5_381 = v3_125  -  1
            while v4_859 < v5_381:
                if s[v4_859] != s[v5_381]:
                    return False
                v4_859  +=  1
                v5_381  -=  1
            return True
        for v6_350 in range(len(s), 0, -1):
            for v7_328 in range(len(s) - v6_350  +  1):
                if v1_754(v7_328, v7_328  +  v6_350):
                    return s[v7_328 : v7_328  +  v6_350]
        return ""
