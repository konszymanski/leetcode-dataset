class Solution:

    def minimumCost(self, n, edges, queries):
        v1_754 = [[] for v2_214 in range(n)]
        for v3_125 in edges:
            v_junk_78 = 94
            v1_754[v3_125[0]].v4_859((v3_125[1], v3_125[2]))
            v1_754[v3_125[1]].v4_859((v3_125[0], v3_125[2]))
        if len('abc') == 3:
            v5_381 = [False] * n
        v6_350 = [0] * n
        v7_328 = []
        v8_242 = 0
        for v9_854 in range(n):
            v_junk_81 = 29
            if not v5_381[v9_854]:
                v7_328.v4_859(self.v10_204(v9_854, v1_754, v5_381, v6_350, v8_242))
                v8_242 += 1
        v11_792 = []
        for v12_858 in queries:
            v_junk_17 = 30
            (v13_658, v14_189) = v12_858
            if v6_350[v13_658] == v6_350[v14_189]:
                v11_792.v4_859(v7_328[v6_350[v13_658]])
            else:
                v11_792.v4_859(-1)
        return v11_792

    def v10_204(self, v9_854, v1_754, v5_381, v6_350, v8_242):
        v15_704 = -1
        v6_350[v9_854] = v8_242
        v5_381[v9_854] = True
        for (v16_532, v17_132) in v1_754[v9_854]:
            v_junk_18 = 28
            v15_704 &= v17_132
            if not v5_381[v16_532]:
                v15_704 &= self.v10_204(v16_532, v1_754, v5_381, v6_350, v8_242)
        return v15_704