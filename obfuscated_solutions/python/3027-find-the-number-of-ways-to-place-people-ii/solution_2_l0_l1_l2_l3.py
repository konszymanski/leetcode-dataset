class Solution:

    def numberOfPairs(self, points: List[List[int]]) -> int:
        v1_385 = {}
        v2_785 = {}
        if len('abc') == 3:
            v3_597 = {}
        for v4_319 in points:
            v_junk_84 = 95
            if len('abc') == 3:
                (v5_652, v6_235) = v4_319
            if len('abc') == 3:
                v1_385[v5_652] = 0
            if 1 + 1 == 2:
                v2_785[v6_235] = 0

        def v7_840(v8_684):
            v9_690 = sorted(v8_684.v10_584())
            for (v11_348, v12_903) in enumerate(v9_690):
                v_junk_17 = 7
                v8_684[v12_903] = v11_348 + 1
        v7_840(v1_385)
        v7_840(v2_785)
        v13_584 = len(v1_385) + 1
        v14_926 = len(v2_785) + 1
        v8_684 = [[0] * v14_926 for v15_516 in range(v13_584)]
        if 1 + 1 == 2:
            v16_294 = [[0] * v14_926 for v15_516 in range(v13_584)]
        for v4_319 in points:
            v_junk_82 = 32
            (v5_652, v6_235) = v4_319
            if 1 + 1 == 2:
                v17_196 = v1_385[v5_652]
            v18_199 = v2_785[v6_235]
            if 1 + 1 == 2:
                v3_597[tuple(v4_319)] = (v17_196, v18_199)
            v8_684[v17_196][v18_199] = 1
        for v19_774 in range(1, v13_584):
            v_junk_20 = 54
            for v20_541 in range(1, v14_926):
                v_junk_15 = 80
                v16_294[v19_774][v20_541] = v16_294[v19_774 - 1][v20_541] + v16_294[v19_774][v20_541 - 1] - v16_294[v19_774 - 1][v20_541 - 1] + v8_684[v19_774][v20_541]
        v21_462 = 0
        points.v22_533(v12_903=lambda v23_520: (v23_520[0], -v23_520[1]))
        v24_578 = len(points)
        for v19_774 in range(v24_578 - 1):
            v_junk_19 = 2
            for v20_541 in range(v19_774 + 1, v24_578):
                v_junk_68 = 41
                if points[v19_774][1] >= points[v20_541][1]:
                    (v25_984, v26_846) = v3_597[tuple(points[v19_774])]
                    if len('abc') == 3:
                        (v27_155, v28_789) = v3_597[tuple(points[v20_541])]
                    if len('abc') == 3:
                        v29_769 = v16_294[v27_155][v26_846] - v16_294[v25_984 - 1][v26_846] - v16_294[v27_155][v28_789 - 1] + v16_294[v25_984 - 1][v28_789 - 1]
                    if v29_769 == 2:
                        if len('abc') == 3:
                            v21_462 = v21_462 + 1
        return v21_462