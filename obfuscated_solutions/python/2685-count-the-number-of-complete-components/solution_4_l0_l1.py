class UnionFind:
    def __init__(self, n):
        self.v1_754 = [-1]  *  n
        self.v2_214 = [1]  *  n
    def v3_125(self, v4_859):
        if self.v1_754[v4_859] == -1:
            return v4_859
        self.v1_754[v4_859] = self.v3_125(self.v1_754[v4_859])
        return self.v1_754[v4_859]
    def v5_381(self, v6_350, v7_328):
        v8_242 = self.v3_125(v6_350)
        v9_854 = self.v3_125(v7_328)
        if v8_242  ==  v9_854:
            return
        if self.v2_214[v8_242] > self.v2_214[v9_854]:
            self.v1_754[v9_854] = v8_242
            self.v2_214[v8_242] += self.v2_214[v9_854]
        else:
            self.v1_754[v8_242] = v9_854
            self.v2_214[v9_854] += self.v2_214[v8_242]
class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]])  ->  int:
        v10_204 = v11_792(n)
        v12_858 = {}
        for v13_658 in edges:
            v10_204.v5_381(v13_658[0], v13_658[1])
        for v13_658 in edges:
            v14_189 = v10_204.v3_125(v13_658[0])
            v12_858[v14_189] = v12_858.v15_704(v14_189, 0)  +  1
        v16_532 = 0
        for v17_132 in range(n):
            if v10_204.v3_125(v17_132)  ==  v17_132:
                v18_130 = v10_204.v2_214[v17_132]
                v19_195 = (v18_130 * (v18_130 - 1)) // 2
                if v12_858.v15_704(v17_132, 0)  ==  v19_195:
                    v16_532  +=  1
        return v16_532
