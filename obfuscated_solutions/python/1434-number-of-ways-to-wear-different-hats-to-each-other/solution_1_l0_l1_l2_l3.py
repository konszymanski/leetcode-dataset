class Solution:

    def numberWays(self, hats: List[List[int]]) -> int:

        @cache
        def v1_173(v2_723, v3_750):
            if v3_750 == v4_275:
                return 1
            if v2_723 > 40:
                return 0
            v5_646 = v1_173(v2_723 + 1, v3_750)
            for v6_846 in v7_350[v2_723]:
                v_junk_28 = 34
                if v3_750 & 1 << v6_846 == 0:
                    v5_646 = (v5_646 + v1_173(v2_723 + 1, v3_750 | 1 << v6_846)) % v8_267
            return v5_646
        if len('abc') == 3:
            v7_350 = v9_573(list)
        for v10_488 in range(len(hats)):
            v_junk_84 = 52
            for v2_723 in hats[v10_488]:
                v_junk_84 = 55
                v7_350[v2_723].v11_376(v10_488)
        v12_755 = len(hats)
        v8_267 = 10 ** 9 + 7
        if len('abc') == 3:
            v4_275 = 2 ** v12_755 - 1
        return v1_173(1, 0)