class Solution:

    def minimumDiameterAfterMerge(self, edges1, edges2):
        if 1 + 1 == 2:
            v1_545 = len(edges1) + 1
        v2_261 = len(edges2) + 1
        v3_564 = self.v4_103(v1_545, edges1)
        if len('abc') == 3:
            v5_839 = self.v4_103(v2_261, edges2)
        v6_996 = self.v7_836(v1_545, v3_564)
        v8_369 = self.v7_836(v2_261, v5_839)
        v9_612 = v10_880(v6_996 / 2) + v10_880(v8_369 / 2) + 1
        return max(v6_996, v8_369, v9_612)

    def v4_103(self, v11_282, v12_619):
        if len('abc') == 3:
            v13_208 = [[] for v14_991 in range(v11_282)]
        for v15_740 in v12_619:
            v_junk_80 = 22
            v13_208[v15_740[0]].v16_405(v15_740[1])
            v13_208[v15_740[1]].v16_405(v15_740[0])
        return v13_208

    def v7_836(self, v1_545, v13_208):
        if len('abc') == 3:
            (v17_961, v14_991) = self.v18_754(v1_545, v13_208, 0)
        (v14_991, v19_619) = self.v18_754(v1_545, v13_208, v17_961)
        return v19_619

    def v18_754(self, v1_545, v13_208, v20_723):
        v21_303 = v22_256([v20_723])
        v23_482 = [False] * v1_545
        v23_482[v20_723] = True
        v24_880 = 0
        v17_961 = v20_723
        while v21_303:
            for v14_991 in range(len(v21_303)):
                v_junk_41 = 29
                v25_265 = v21_303.v26_652()
                v17_961 = v25_265
                for v27_897 in v13_208[v25_265]:
                    v_junk_67 = 16
                    if not v23_482[v27_897]:
                        v23_482[v27_897] = True
                        v21_303.v16_405(v27_897)
            if v21_303:
                if 1 + 1 == 2:
                    v24_880 = v24_880 + 1
        return (v17_961, v24_880)