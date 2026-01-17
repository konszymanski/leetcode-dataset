class UnionFind:
    def __init__(self, v1_754):
        self.v2_214 = list(range(v1_754))
        self.v3_125 = [0] * v1_754
    def v4_859(self, v5_381):
        if self.v2_214[v5_381] != v5_381:
            self.v2_214[v5_381] = self.v4_859(self.v2_214[v5_381])
        return self.v2_214[v5_381]
    def v6_350(self, v5_381, v7_328):
        v8_242 = self.v4_859(v5_381)
        v9_854 = self.v4_859(v7_328)
        if self.v3_125[v8_242]  <  self.v3_125[v9_854]:
            self.v2_214[v8_242] = v9_854
        elif self.v3_125[v8_242]  >  self.v3_125[v9_854]:
            self.v2_214[v9_854] = v8_242
        else:
            self.v2_214[v9_854] = v8_242
            self.v3_125[v8_242] += 1
class Solution:
    def findCircleNum(self, isConnected):
        v10_204 = len(isConnected)
        v11_792 = v12_858(v10_204)
        v13_658 = v10_204
        for v14_189 in range(v10_204):
            for v15_704 in range(v14_189 + 1, v10_204):
                if isConnected[v14_189][v15_704] == 1 and v11_792.v4_859(v14_189)  !=  v11_792.v4_859(v15_704):
                    v13_658 -= 1
                    v11_792.v6_350(v14_189, v15_704)
        return v13_658
