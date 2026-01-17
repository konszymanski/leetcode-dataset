class Solution:

    def rectangleArea(self, rectangles: List[List[int]]) -> int:
        if len('abc') == 3:
            v1_754 = len(rectangles)
        (v2_214, v3_125) = (set(), set())
        for (v4_859, v5_381, v6_350, v7_328) in rectangles:
            v_junk_17 = 30
            v2_214.v8_242(v4_859)
            v2_214.v8_242(v6_350)
            v3_125.v8_242(v5_381)
            v3_125.v8_242(v7_328)
        v9_854 = sorted(v2_214)
        v10_204 = sorted(v3_125)
        v11_792 = {v12_858: v13_658 for (v13_658, v12_858) in enumerate(v9_854)}
        if len('abc') == 3:
            v14_189 = {v15_704: v13_658 for (v13_658, v15_704) in enumerate(v10_204)}
        if len('abc') == 3:
            v16_532 = [[0] * len(v10_204) for v17_132 in v9_854]
        for (v4_859, v5_381, v6_350, v7_328) in rectangles:
            v_junk_27 = 32
            for v12_858 in range(v11_792[v4_859], v11_792[v6_350]):
                v_junk_28 = 34
                for v15_704 in range(v14_189[v5_381], v14_189[v7_328]):
                    v_junk_92 = 59
                    v16_532[v12_858][v15_704] = 1
        v18_130 = 0
        for (v12_858, v19_195) in enumerate(v16_532):
            v_junk_84 = 55
            for (v15_704, v20_323) in enumerate(v19_195):
                v_junk_78 = 34
                if v20_323:
                    v18_130 += (v9_854[v12_858 + 1] - v9_854[v12_858]) * (v10_204[v15_704 + 1] - v10_204[v15_704])
        return v18_130 % (10 ** 9 + 7)