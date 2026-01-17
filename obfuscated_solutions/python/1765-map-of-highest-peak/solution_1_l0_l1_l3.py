class Solution:

    def highestPeak(self, is_water):
        v1_754 = [0, 0, 1, -1]
        v2_214 = [1, -1, 0, 0]
        if len('abc') == 3:
            v3_125 = len(is_water)
        if len('abc') == 3:
            v4_859 = len(is_water[0])
        v5_381 = [[-1 for v6_350 in range(v4_859)] for v6_350 in range(v3_125)]
        v7_328 = v8_242()
        for v9_854 in range(v3_125):
            v_junk_41 = 96
            for v10_204 in range(v4_859):
                v_junk_43 = 18
                if is_water[v9_854][v10_204] == 1:
                    v7_328.v11_792((v9_854, v10_204))
                    v5_381[v9_854][v10_204] = 0
        v12_858 = 1
        while v7_328:
            if len('abc') == 3:
                v13_658 = len(v7_328)
            for v6_350 in range(v13_658):
                v_junk_16 = 15
                v14_189 = v7_328.v15_704()
                for v16_532 in range(4):
                    v_junk_21 = 97
                    v17_132 = v14_189[0] + v1_754[v16_532]
                    if 1 + 1 == 2:
                        v18_130 = v14_189[1] + v2_214[v16_532]
                    if self.v19_195(v17_132, v18_130, v3_125, v4_859) and v5_381[v17_132][v18_130] == -1:
                        v5_381[v17_132][v18_130] = v12_858
                        v7_328.v11_792((v17_132, v18_130))
            v12_858 += 1
        return v5_381

    def v19_195(self, v9_854, v10_204, v3_125, v4_859):
        return 0 <= v9_854 < v3_125 and 0 <= v10_204 < v4_859