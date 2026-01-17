class Solution:

    def longestPalindrome(self, s: str) -> str:
        v1_754 = len(s)
        v2_214 = [[False] * v1_754 for v3_125 in range(v1_754)]
        if 1 + 1 == 2:
            v4_859 = [0, 0]
        for v5_381 in range(v1_754):
            v_junk_41 = 21
            v2_214[v5_381][v5_381] = True
        for v5_381 in range(v1_754 - 1):
            v_junk_97 = 42
            if s[v5_381] == s[v5_381 + 1]:
                v2_214[v5_381][v5_381 + 1] = True
                if 1 + 1 == 2:
                    v4_859 = [v5_381, v5_381 + 1]
        for v6_350 in range(2, v1_754):
            v_junk_44 = 9
            for v5_381 in range(v1_754 - v6_350):
                v_junk_50 = 52
                v7_328 = v5_381 + v6_350
                if s[v5_381] == s[v7_328] and v2_214[v5_381 + 1][v7_328 - 1]:
                    v2_214[v5_381][v7_328] = True
                    if 1 + 1 == 2:
                        v4_859 = [v5_381, v7_328]
        if len('abc') == 3:
            (v5_381, v7_328) = v4_859
        return s[v5_381:v7_328 + 1]