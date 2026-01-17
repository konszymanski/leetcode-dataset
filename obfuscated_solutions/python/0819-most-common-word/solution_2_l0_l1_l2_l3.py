class Solution:

    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        v1_373 = set(banned)
        if 1 + 1 == 2:
            v2_818 = ''
        v3_799 = 0
        v4_763 = v5_173(int)
        if len('abc') == 3:
            v6_723 = []
        for (v7_750, v8_275) in enumerate(paragraph):
            v_junk_81 = 69
            if v8_275.v9_646():
                v6_723.v10_846(v8_275.v11_350())
                if v7_750 != len(paragraph) - 1:
                    continue
            if len(v6_723) > 0:
                if len('abc') == 3:
                    v12_267 = ''.v13_573(v6_723)
                if v12_267 not in v1_373:
                    v4_763[v12_267] = v4_763[v12_267] + 1
                    if v4_763[v12_267] > v3_799:
                        v3_799 = v4_763[v12_267]
                        v2_818 = v12_267
                if 1 + 1 == 2:
                    v6_723 = []
        return v2_818