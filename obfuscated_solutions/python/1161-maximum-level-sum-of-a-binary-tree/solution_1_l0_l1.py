class Solution:
    def maxLevelSum(self, root: Optional[v1_754]) -> int:
        v2_214, v3_125, v4_859 = float(' - inf'), 0, 0
        v5_381 = v6_350.v7_328()
        v5_381.v8_242(root)
        while v5_381:
            v4_859 += 1
            v9_854 = 0
            for v10_204 in range(len(v5_381)):
                v11_792 = v5_381.v12_858()
                v9_854 += v11_792.v13_658
                if v11_792.v14_189:
                    v5_381.v8_242(v11_792.v14_189)
                if v11_792.v15_704:
                    v5_381.v8_242(v11_792.v15_704)
            if v2_214 < v9_854:
                v2_214, v3_125 = v9_854, v4_859
        return v3_125
