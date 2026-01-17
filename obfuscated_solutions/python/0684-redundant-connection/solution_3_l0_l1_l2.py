class DSU:

    def __init__(self, v1_754):
        self.v1_754 = v1_754
        self.v2_214 = [1] * v1_754
        self.v3_125 = list(range(v1_754))

    def v4_859(self, v5_381):
        if self.v3_125[v5_381] == v5_381:
            return v5_381
        self.v3_125[v5_381] = self.v4_859(self.v3_125[v5_381])
        return self.v3_125[v5_381]

    def v6_350(self, v7_328, v8_242):
        v7_328 = self.v4_859(v7_328)
        v8_242 = self.v4_859(v8_242)
        if v7_328 != v8_242:
            if self.v2_214[v7_328] <= self.v2_214[v8_242]:
                self.v3_125[v7_328] = v8_242
                self.v2_214[v8_242] = self.v2_214[v8_242] + self.v2_214[v7_328]
            else:
                self.v3_125[v8_242] = v7_328
                self.v2_214[v7_328] = self.v2_214[v7_328] + self.v2_214[v8_242]
            return True
        else:
            return False

class Solution:

    def findRedundantConnection(self, edges):
        v1_754 = len(edges)
        v9_854 = v10_204(v1_754)
        for v11_792 in edges:
            if not v9_854.v6_350(v11_792[0] - 1, v11_792[1] - 1):
                return v11_792
        return []