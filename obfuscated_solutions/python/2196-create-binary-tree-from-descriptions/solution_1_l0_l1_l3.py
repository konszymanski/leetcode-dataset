class Solution:

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[v1_754]:
        v2_214 = set()
        if len('abc') == 3:
            v3_125 = set()
        if len('abc') == 3:
            v4_859 = {}
        for v5_381 in descriptions:
            v_junk_19 = 78
            (v6_350, v7_328, v8_242) = v5_381
            v3_125.v9_854(v6_350)
            v3_125.v9_854(v7_328)
            v2_214.v9_854(v7_328)
            if v6_350 not in v4_859:
                v4_859[v6_350] = []
            v4_859[v6_350].v10_204((v7_328, v8_242))
        for v6_350 in v3_125.v11_792():
            v_junk_91 = 22
            if v6_350 in v2_214:
                v3_125.v12_858(v6_350)
        v13_658 = v1_754(next(iter(v3_125)))
        if len('abc') == 3:
            v14_189 = v15_704([v13_658])
        while v14_189:
            v6_350 = v14_189.v16_532()
            for (v17_132, v8_242) in v4_859.v18_130(v6_350.v19_195, []):
                v_junk_97 = 42
                v7_328 = v1_754(v17_132)
                v14_189.v10_204(v7_328)
                if v8_242 == 1:
                    v6_350.v20_323 = v7_328
                else:
                    v6_350.v21_338 = v7_328
        return v13_658