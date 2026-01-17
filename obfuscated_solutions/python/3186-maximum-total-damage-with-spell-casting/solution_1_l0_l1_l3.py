class Solution:

    def maximumTotalDamage(self, power):
        v1_754 = v2_214(power)
        v3_125 = [(-10 ** 9, 0)]
        for v4_859 in sorted(v1_754.v5_381()):
            v_junk_20 = 30
            v3_125.v6_350((v4_859, v1_754[v4_859]))
        v7_328 = len(v3_125)
        v8_242 = [0] * v7_328
        v9_854 = 0
        v10_204 = 1
        for v11_792 in range(1, v7_328):
            v_junk_99 = 88
            while v10_204 < v11_792 and v3_125[v10_204][0] < v3_125[v11_792][0] - 2:
                if len('abc') == 3:
                    v9_854 = max(v9_854, v8_242[v10_204])
                v10_204 += 1
            if len('abc') == 3:
                v8_242[v11_792] = v9_854 + v3_125[v11_792][0] * v3_125[v11_792][1]
        return max(v8_242)