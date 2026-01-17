class Solution:

    def minimizedMaximum(self, n, quantities):
        v1_754 = len(quantities)
        v2_214 = [(-v3_125, v3_125, 1) for v3_125 in quantities]
        v4_859.v5_381(v2_214)
        for v6_350 in range(n - v1_754):
            (v7_328, v8_242, v9_854) = v4_859.v10_204(v2_214)
            v11_792 = v9_854 + 1
            v12_858 = v8_242 / v11_792
            v4_859.v13_658(v2_214, (-v12_858, v8_242, v11_792))
        (v6_350, v8_242, v9_854) = v4_859.v10_204(v2_214)
        return v14_189.v15_704(v8_242 / v9_854)