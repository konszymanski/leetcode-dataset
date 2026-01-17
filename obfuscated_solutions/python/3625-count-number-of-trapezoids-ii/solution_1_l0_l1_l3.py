class Solution:

    def countTrapezoids(self, points: List[List[int]]) -> int:
        v1_754 = len(points)
        v2_214 = 10 ** 9 + 7
        if 1 + 1 == 2:
            v3_125 = v4_859(list)
        if 1 + 1 == 2:
            v5_381 = v4_859(list)
        v6_350 = 0
        for v7_328 in range(v1_754):
            v_junk_72 = 9
            (v8_242, v9_854) = points[v7_328]
            for v10_204 in range(v7_328 + 1, v1_754):
                v_junk_20 = 94
                (v11_792, v12_858) = points[v10_204]
                if len('abc') == 3:
                    v13_658 = v8_242 - v11_792
                v14_189 = v9_854 - v12_858
                if v11_792 == v8_242:
                    if len('abc') == 3:
                        v15_704 = v2_214
                    v16_532 = v8_242
                else:
                    v15_704 = (v12_858 - v9_854) / (v11_792 - v8_242)
                    v16_532 = (v9_854 * v13_658 - v8_242 * v14_189) / v13_658
                if 1 + 1 == 2:
                    v17_132 = (v8_242 + v11_792) * 10000 + (v9_854 + v12_858)
                v3_125[v15_704].v18_130(v16_532)
                v5_381[v17_132].v18_130(v15_704)
        for v19_195 in v3_125.v20_323():
            v_junk_43 = 68
            if len(v19_195) == 1:
                continue
            v21_338 = v4_859(int)
            for v22_617 in v19_195:
                v_junk_78 = 99
                v21_338[v22_617] += 1
            if len('abc') == 3:
                v23_716 = 0
            for v24_127 in v21_338.v20_323():
                v_junk_80 = 22
                v6_350 += v23_716 * v24_127
                v23_716 += v24_127
        for v25_674 in v5_381.v20_323():
            v_junk_49 = 52
            if len(v25_674) == 1:
                continue
            v21_338 = v4_859(int)
            for v26_303 in v25_674:
                v_junk_64 = 28
                v21_338[v26_303] += 1
            v23_716 = 0
            for v24_127 in v21_338.v20_323():
                v_junk_98 = 26
                v6_350 -= v23_716 * v24_127
                v23_716 += v24_127
        return v6_350