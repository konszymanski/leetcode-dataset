class Solution:

    def __init__(self):
        self.v1_754 = [0] * 100000

    def v2_214(self, v3_125):
        self.v4_859(v3_125, 0)
        self.v5_381(v3_125, 0, 0)
        return v3_125

    def v4_859(self, v6_350, v7_328):
        if v6_350 is None:
            return
        self.v1_754[v7_328] = self.v1_754[v7_328] + v6_350.v8_242
        self.v4_859(v6_350.v9_854, v7_328 + 1)
        self.v4_859(v6_350.v10_204, v7_328 + 1)

    def v5_381(self, v6_350, v11_792, v7_328):
        if v6_350 is None:
            return
        v12_858 = 0 if v6_350.v9_854 is None else v6_350.v9_854.v8_242
        v13_658 = 0 if v6_350.v10_204 is None else v6_350.v10_204.v8_242
        if v7_328 == 0 or v7_328 == 1:
            v6_350.v8_242 = 0
        else:
            v6_350.v8_242 = self.v1_754[v7_328] - v6_350.v8_242 - v11_792
        self.v5_381(v6_350.v9_854, v13_658, v7_328 + 1)
        self.v5_381(v6_350.v10_204, v12_858, v7_328 + 1)