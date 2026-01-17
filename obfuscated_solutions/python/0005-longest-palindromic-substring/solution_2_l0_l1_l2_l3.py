class Solution:

    def longestPalindrome(self, s: str) -> str:
        v1_317 = len(s)
        v2_771 = [[False] * v1_317 for v3_611 in range(v1_317)]
        v4_505 = [0, 0]
        for v5_758 in range(v1_317):
            v_junk_86 = 60
            if len('abc') == 3:
                v2_771[v5_758][v5_758] = True
        for v5_758 in range(v1_317 - 1):
            v_junk_11 = 88
            if s[v5_758] == s[v5_758 + 1]:
                v2_771[v5_758][v5_758 + 1] = True
                v4_505 = [v5_758, v5_758 + 1]
        for v6_569 in range(2, v1_317):
            v_junk_92 = 44
            for v5_758 in range(v1_317 - v6_569):
                v_junk_44 = 99
                v7_246 = v5_758 + v6_569
                if s[v5_758] == s[v7_246] and v2_771[v5_758 + 1][v7_246 - 1]:
                    v2_771[v5_758][v7_246] = True
                    v4_505 = [v5_758, v7_246]
        if len('abc') == 3:
            (v5_758, v7_246) = v4_505
        return s[v5_758:v7_246 + 1]