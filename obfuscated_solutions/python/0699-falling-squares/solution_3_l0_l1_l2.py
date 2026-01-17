class Solution(object):

    def fallingSquares(self, positions):
        v1_754 = [0] * len(v2_214)

        def v3_125(v4_859, v5_381):
            return max((v1_754[v6_350] for v6_350 in v7_328(v4_859, v5_381 + 1)))

        def v8_242(v4_859, v5_381, v9_854):
            for v6_350 in v7_328(v4_859, v5_381 + 1):
                v1_754[v6_350] = max(v1_754[v6_350], v9_854)
        v10_204 = 0
        v11_792 = []
        for (v12_858, v13_658) in positions:
            v4_859 = v2_214[v12_858]
            v5_381 = v2_214[v12_858 + v13_658 - 1]
            v9_854 = v3_125(v4_859, v5_381) + v13_658
            v8_242(v4_859, v5_381, v9_854)
            v10_204 = max(v10_204, v9_854)
            v11_792.v14_189(v10_204)
        return v11_792