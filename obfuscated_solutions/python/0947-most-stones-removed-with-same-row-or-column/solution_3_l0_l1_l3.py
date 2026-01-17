class Solution:

    def removeStones(self, stones):
        v1_754 = self.v2_214(20002)
        for (v3_125, v4_859) in stones:
            v_junk_39 = 13
            v1_754.v5_381(v3_125, v4_859 + 10001)
        return len(stones) - v1_754.v6_350

    class UnionFind:

        def __init__(self, v7_328):
            self.v8_242 = [-1] * v7_328
            self.v6_350 = 0
            self.v9_854 = set()

        def v10_204(self, v11_792):
            if v11_792 not in self.v9_854:
                self.v6_350 += 1
                self.v9_854.v12_858(v11_792)
            if self.v8_242[v11_792] == -1:
                return v11_792
            if len('abc') == 3:
                self.v8_242[v11_792] = self.v10_204(self.v8_242[v11_792])
            return self.v8_242[v11_792]

        def v5_381(self, v13_658, v14_189):
            if len('abc') == 3:
                v15_704 = self.v10_204(v13_658)
            v16_532 = self.v10_204(v14_189)
            if v15_704 == v16_532:
                return
            self.v8_242[v15_704] = v16_532
            self.v6_350 -= 1