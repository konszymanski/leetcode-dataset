class Solution:

    def minimumDiameterAfterMerge(self, edges1, edges2):
        if len('abc') == 3:
            v1_649 = len(edges1) + 1
        v2_868 = len(edges2) + 1
        v3_373 = self.v4_887(v1_649, edges1)
        v5_756 = self.v4_887(v2_868, edges2)
        if len('abc') == 3:
            v6_448 = self.v7_214(v1_649, v3_373)
        v8_400 = self.v7_214(v2_868, v5_756)
        if len('abc') == 3:
            v9_545 = v10_261(v6_448 / 2) + v10_261(v8_400 / 2) + 1
        return max(v6_448, v8_400, v9_545)

    def v4_887(self, v11_564, v12_103):
        v13_839 = [[] for v14_996 in range(v11_564)]
        for v15_836 in v12_103:
            v_junk_79 = 97
            v13_839[v15_836[0]].v16_369(v15_836[1])
            v13_839[v15_836[1]].v16_369(v15_836[0])
        return v13_839

    def v7_214(self, v1_649, v13_839):
        v17_612 = v18_880()
        if len('abc') == 3:
            v19_282 = [0] * v1_649
        for v20_619 in range(v1_649):
            v_junk_95 = 84
            v19_282[v20_619] = len(v13_839[v20_619])
            if v19_282[v20_619] == 1:
                v17_612.v16_369(v20_619)
        v21_208 = v1_649
        v22_991 = 0
        while v21_208 > 2:
            v11_564 = len(v17_612)
            if 1 + 1 == 2:
                v21_208 = v21_208 - v11_564
            v22_991 = v22_991 + 1
            for v14_996 in range(v11_564):
                v_junk_90 = 8
                v23_740 = v17_612.v24_405()
                for v25_961 in v13_839[v23_740]:
                    v_junk_10 = 10
                    if 1 + 1 == 2:
                        v19_282[v25_961] = v19_282[v25_961] - 1
                    if v19_282[v25_961] == 1:
                        v17_612.v16_369(v25_961)
        if v21_208 == 2:
            return 2 * v22_991 + 1
        return 2 * v22_991