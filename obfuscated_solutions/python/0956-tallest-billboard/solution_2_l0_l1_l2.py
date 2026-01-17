class Solution:

    def tallestBillboard(self, rods: List[int]) -> int:
        v1_754 = {0: 0}
        for v2_214 in rods:
            v3_125 = v1_754.v4_859()
            for (v5_381, v6_350) in v1_754.v7_328():
                v8_242 = v6_350 - v5_381
                v3_125[v5_381 + v2_214] = max(v3_125.v9_854(v5_381 + v2_214, 0), v6_350 + v2_214)
                v10_204 = abs(v8_242 + v2_214 - v6_350)
                v11_792 = max(v8_242 + v2_214, v6_350)
                v3_125[v10_204] = max(v3_125.v9_854(v10_204, 0), v11_792)
            v1_754 = v3_125
        return v1_754.v9_854(0, 0)