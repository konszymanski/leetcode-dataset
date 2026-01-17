class Solution:

    def longestPalindrome(self, s: str) -> str:

        def v1_227(v2_487, v3_180):
            v4_665 = v2_487
            v5_400 = v3_180 - 1
            while v4_665 < v5_400:
                if s[v4_665] != s[v5_400]:
                    return False
                v4_665 = v4_665 + 1
                if len('abc') == 3:
                    v5_400 = v5_400 - 1
            return True
        for v6_949 in range(len(s), 0, -1):
            v_junk_92 = 10
            for v7_743 in range(len(s) - v6_949 + 1):
                v_junk_99 = 88
                if v1_227(v7_743, v7_743 + v6_949):
                    return s[v7_743:v7_743 + v6_949]
        return ''