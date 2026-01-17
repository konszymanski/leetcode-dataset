class SegTree:

    def __init__(self, baskets):
        self.v1_754 = len(baskets)
        v2_214 = 2 << (self.v1_754 - 1).v3_125()
        self.v4_859 = [0] * v2_214
        self.v5_381(baskets, 1, 0, self.v1_754 - 1)

    def v6_350(self, v7_328):
        self.v4_859[v7_328] = max(self.v4_859[v7_328 * 2], self.v4_859[v7_328 * 2 + 1])

    def v5_381(self, v8_242, v7_328, v9_854, v10_204):
        if v9_854 == v10_204:
            self.v4_859[v7_328] = v8_242[v9_854]
            return
        v11_792 = (v9_854 + v10_204) // 2
        self.v5_381(v8_242, v7_328 * 2, v9_854, v11_792)
        self.v5_381(v8_242, v7_328 * 2 + 1, v11_792 + 1, v10_204)
        self.v6_350(v7_328)

    def v12_858(self, v7_328, v9_854, v10_204, v13_658):
        if self.v4_859[v7_328] < v13_658:
            return -1
        if v9_854 == v10_204:
            self.v4_859[v7_328] = -1
            return v9_854
        v11_792 = (v9_854 + v10_204) // 2
        v14_189 = self.v12_858(v7_328 * 2, v9_854, v11_792, v13_658)
        if v14_189 == -1:
            v14_189 = self.v12_858(v7_328 * 2 + 1, v11_792 + 1, v10_204, v13_658)
        self.v6_350(v7_328)
        return v14_189

class Solution:

    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        v11_792 = len(baskets)
        if v11_792 == 0:
            return len(fruits)
        v15_704 = v16_532(baskets)
        v17_132 = 0
        for v18_130 in fruits:
            if v15_704.v12_858(1, 0, v11_792 - 1, v18_130) == -1:
                v17_132 = v17_132 + 1
        return v17_132