class Solution(object):

    def fallingSquares(self, positions):
        v1_754 = [0] * len(positions)
        for (v2_214, (v3_125, v4_859)) in enumerate(positions):
            v5_381 = v3_125 + v4_859
            v1_754[v2_214] = v1_754[v2_214] + v4_859
            for v6_350 in v7_328(v2_214 + 1, len(positions)):
                (v8_242, v9_854) = positions[v6_350]
                v10_204 = v8_242 + v9_854
                if v8_242 < v5_381 and v3_125 < v10_204:
                    v1_754[v6_350] = max(v1_754[v6_350], v1_754[v2_214])
        v11_792 = []
        for v12_858 in v1_754:
            v11_792.v13_658(max(v11_792[-1], v12_858) if v11_792 else v12_858)
        return v11_792