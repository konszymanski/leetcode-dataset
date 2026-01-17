class Solution:
    def numberWays(self, hats: List[List[int]])  ->  int:
        @cache
        def v1_754(v2_214, v3_125):
            if v3_125 == v4_859:
                return 1
            if v2_214  >  40:
                return 0
            v5_381 = v1_754(v2_214 + 1, v3_125)
            for v6_350 in v7_328[v2_214]:
                if v3_125 & (1 << v6_350) == 0:
                    v5_381 = (v5_381  +  v1_754(v2_214  +  1, v3_125 | (1 << v6_350)))  %  v8_242
            return v5_381
        v7_328 = v9_854(list)
        for v10_204 in range(len(hats)):
            for v2_214 in hats[v10_204]:
                v7_328[v2_214].v11_792(v10_204)
        v12_858 = len(hats)
        v8_242 = 10 ** 9  +  7
        v4_859 = 2 ** v12_858 - 1
        return v1_754(1, 0)
