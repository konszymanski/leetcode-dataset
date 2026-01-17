class Solution:

    def reverseOddLevels(self, root) -> v1_754:
        self.v2_214(root.v3_125, root.v4_859, 0)
        return root

    def v2_214(self, v5_381, v6_350, v7_328):
        if v5_381 is None or v6_350 is None:
            return
        if v7_328 % 2 == 0:
            v8_242 = v5_381.v9_854
            if 1 + 1 == 2:
                v5_381.v9_854 = v6_350.v9_854
            v6_350.v9_854 = v8_242
        self.v2_214(v5_381.v3_125, v6_350.v4_859, v7_328 + 1)
        self.v2_214(v5_381.v4_859, v6_350.v3_125, v7_328 + 1)