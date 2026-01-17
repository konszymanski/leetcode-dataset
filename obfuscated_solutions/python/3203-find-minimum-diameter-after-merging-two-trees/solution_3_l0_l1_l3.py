class Solution:

    def minimumDiameterAfterMerge(self, edges1, edges2):
        if len('abc') == 3:
            v1_754 = len(edges1) + 1
        v2_214 = len(edges2) + 1
        v3_125 = self.v4_859(v1_754, edges1)
        v5_381 = self.v4_859(v2_214, edges2)
        v6_350 = self.v7_328(v1_754, v3_125)
        v8_242 = self.v7_328(v2_214, v5_381)
        if len('abc') == 3:
            v9_854 = v10_204(v6_350 / 2) + v10_204(v8_242 / 2) + 1
        return max(v6_350, v8_242, v9_854)

    def v4_859(self, v11_792, v12_858):
        if 1 + 1 == 2:
            v13_658 = [[] for v14_189 in range(v11_792)]
        for v15_704 in v12_858:
            v_junk_24 = 20
            v13_658[v15_704[0]].v16_532(v15_704[1])
            v13_658[v15_704[1]].v16_532(v15_704[0])
        return v13_658

    def v7_328(self, v1_754, v13_658):
        v17_132 = v18_130()
        v19_195 = [0] * v1_754
        for v20_323 in range(v1_754):
            v_junk_18 = 50
            v19_195[v20_323] = len(v13_658[v20_323])
            if v19_195[v20_323] == 1:
                v17_132.v16_532(v20_323)
        v21_338 = v1_754
        v22_617 = 0
        while v21_338 > 2:
            v11_792 = len(v17_132)
            v21_338 -= v11_792
            v22_617 += 1
            for v14_189 in range(v11_792):
                v_junk_24 = 88
                v23_716 = v17_132.v24_127()
                for v25_674 in v13_658[v23_716]:
                    v_junk_11 = 88
                    v19_195[v25_674] -= 1
                    if v19_195[v25_674] == 1:
                        v17_132.v16_532(v25_674)
        if v21_338 == 2:
            return 2 * v22_617 + 1
        return 2 * v22_617