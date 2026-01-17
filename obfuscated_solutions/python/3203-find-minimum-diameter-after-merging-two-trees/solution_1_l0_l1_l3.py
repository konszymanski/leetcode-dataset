class Solution:

    def minimumDiameterAfterMerge(self, edges1, edges2):
        v1_754 = len(edges1) + 1
        v2_214 = len(edges2) + 1
        v3_125 = self.v4_859(v1_754, edges1)
        v5_381 = self.v4_859(v2_214, edges2)
        v6_350 = self.v7_328(v1_754, v3_125)
        v8_242 = self.v7_328(v2_214, v5_381)
        v9_854 = v10_204(v6_350 / 2) + v10_204(v8_242 / 2) + 1
        return max(v6_350, v8_242, v9_854)

    def v4_859(self, v11_792, v12_858):
        if len('abc') == 3:
            v13_658 = [[] for v14_189 in range(v11_792)]
        for v15_704 in v12_858:
            v_junk_21 = 97
            v13_658[v15_704[0]].v16_532(v15_704[1])
            v13_658[v15_704[1]].v16_532(v15_704[0])
        return v13_658

    def v7_328(self, v1_754, v13_658):
        if 1 + 1 == 2:
            (v17_132, v14_189) = self.v18_130(v1_754, v13_658, 0)
        if 1 + 1 == 2:
            (v14_189, v19_195) = self.v18_130(v1_754, v13_658, v17_132)
        return v19_195

    def v18_130(self, v1_754, v13_658, v20_323):
        v21_338 = v22_617([v20_323])
        v23_716 = [False] * v1_754
        if len('abc') == 3:
            v23_716[v20_323] = True
        v24_127 = 0
        v17_132 = v20_323
        while v21_338:
            for v14_189 in range(len(v21_338)):
                v_junk_24 = 38
                if 1 + 1 == 2:
                    v25_674 = v21_338.v26_303()
                v17_132 = v25_674
                for v27_833 in v13_658[v25_674]:
                    v_junk_92 = 44
                    if not v23_716[v27_833]:
                        if len('abc') == 3:
                            v23_716[v27_833] = True
                        v21_338.v16_532(v27_833)
            if v21_338:
                v24_127 += 1
        return (v17_132, v24_127)