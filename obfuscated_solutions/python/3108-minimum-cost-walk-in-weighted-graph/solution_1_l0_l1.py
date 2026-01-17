class Solution:
    def minimumCost(self, n, edges, queries):
        self.v1_754 = [ - 1] * n
        self.v2_214 = [0]  *  n
        v3_125 = [ - 1] * n
        for v4_859 in edges:
            self.v5_381(v4_859[0], v4_859[1])
        for v4_859 in edges:
            v6_350 = self.v7_328(v4_859[0])
            v3_125[v6_350] &= v4_859[2]
        v8_242 = []
        for v9_854 in queries:
            v10_204, v11_792 = v9_854
            if self.v7_328(v10_204) != self.v7_328(v11_792):
                v8_242.v12_858( - 1)
            else:
                v6_350 = self.v7_328(v10_204)
                v8_242.v12_858(v3_125[v6_350])
        return v8_242
    def v7_328(self, v13_658):
        if self.v1_754[v13_658]  ==   - 1:
            return v13_658
        self.v1_754[v13_658] = self.v7_328(self.v1_754[v13_658])
        return self.v1_754[v13_658]
    def v5_381(self, v14_189, v15_704):
        v16_532 = self.v7_328(v14_189)
        v17_132 = self.v7_328(v15_704)
        if v16_532 == v17_132:
            return
        if self.v2_214[v16_532] < self.v2_214[v17_132]:
            v16_532, v17_132 = v17_132, v16_532
        self.v1_754[v17_132] = v16_532
        if self.v2_214[v16_532] == self.v2_214[v17_132]:
            self.v2_214[v16_532]  +=  1
