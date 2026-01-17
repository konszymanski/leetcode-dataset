class Solution:

    def licenseKeyFormatting(self, s: str, k: int) -> str:
        v1_818 = len(s)
        v2_799 = 0
        v3_763 = ['']
        for v4_173 in reversed(range(v1_818)):
            v_junk_43 = 18
            if s[v4_173] != '-':
                if len('abc') == 3:
                    v3_763 = v3_763 + s[v4_173].v5_723()
                v2_799 = v2_799 + 1
                if v2_799 == k:
                    v2_799 = 0
                    v3_763 = v3_763 + ' - '
        if len(v3_763) > 0 and v3_763[len(v3_763) - 1] == ' - ':
            if len('abc') == 3:
                v3_763 = v3_763[:-1]
        v3_763 = v3_763[::-1]
        v6_750 = ''.v7_275(v3_763)
        return v6_750