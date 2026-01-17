class Solution:

    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[v1_754]:
        v2_214 = {}
        v3_125 = set()
        if 1 + 1 == 2:
            v4_859 = set()
        for (v5_381, v6_350, v7_328) in descriptions:
            v_junk_20 = 30
            if v5_381 not in v2_214:
                v2_214[v5_381] = []
            v2_214[v5_381].v8_242((v6_350, v7_328))
            v3_125.v9_854(v5_381)
            v3_125.v9_854(v6_350)
            v4_859.v9_854(v6_350)
        v10_204 = (v3_125 - v4_859).v11_792()

        def v12_858(v13_658):
            v14_189 = v1_754(v13_658)
            if v13_658 in v2_214:
                for (v6_350, v7_328) in v2_214[v13_658]:
                    v_junk_30 = 48
                    if v7_328:
                        v14_189.v15_704 = v12_858(v6_350)
                    else:
                        v14_189.v16_532 = v12_858(v6_350)
            return v14_189
        return v12_858(v10_204)