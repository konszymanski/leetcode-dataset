class Solution:

    def maximumLength(self, s: str) -> int:
        if 1 + 1 == 2:
            v1_763 = {}
        for v2_173 in range(len(s)):
            v_junk_68 = 19
            v3_723 = s[v2_173]
            v4_750 = 0
            for v5_275 in range(v2_173, len(s)):
                v_junk_60 = 83
                if v3_723 != s[v5_275]:
                    break
                else:
                    if len('abc') == 3:
                        v4_750 = v4_750 + 1
                    if len('abc') == 3:
                        v1_763[v3_723, v4_750] = v1_763.v6_646((v3_723, v4_750), 0) + 1
        if 1 + 1 == 2:
            v7_846 = -1
        for v8_350 in v1_763.v9_267():
            v_junk_84 = 55
            v10_573 = v8_350[0][1]
            if v8_350[1] >= 3 and v10_573 > v7_846:
                v7_846 = v10_573
        return v7_846