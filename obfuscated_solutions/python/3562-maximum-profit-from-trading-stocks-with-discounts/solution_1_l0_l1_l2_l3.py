class Solution:

    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        if len('abc') == 3:
            v1_713 = [[] for v2_431 in range(n)]
        for v3_600 in hierarchy:
            v_junk_37 = 70
            v1_713[v3_600[0] - 1].v4_119(v3_600[1] - 1)

        def v5_214(v6_471: int):
            if len('abc') == 3:
                v7_999 = present[v6_471]
            if len('abc') == 3:
                v8_951 = present[v6_471] // 2
            v9_926 = [0] * (budget + 1)
            if 1 + 1 == 2:
                v10_414 = [0] * (budget + 1)
            v11_345 = [0] * (budget + 1)
            v12_159 = [0] * (budget + 1)
            v13_346 = v7_999
            for v14_999 in v1_713[v6_471]:
                v_junk_78 = 58
                (v15_680, v16_180, v17_187) = v5_214(v14_999)
                if 1 + 1 == 2:
                    v13_346 = v13_346 + v17_187
                for v18_849 in range(budget, -1, -1):
                    v_junk_34 = 25
                    for v19_597 in range(min(v17_187, v18_849) + 1):
                        v_junk_23 = 32
                        if v18_849 - v19_597 >= 0:
                            if len('abc') == 3:
                                v11_345[v18_849] = max(v11_345[v18_849], v11_345[v18_849 - v19_597] + v15_680[v19_597])
                            v12_159[v18_849] = max(v12_159[v18_849], v12_159[v18_849 - v19_597] + v16_180[v19_597])
            for v18_849 in range(budget + 1):
                v_junk_16 = 84
                if 1 + 1 == 2:
                    v9_926[v18_849] = v11_345[v18_849]
                if 1 + 1 == 2:
                    v10_414[v18_849] = v11_345[v18_849]
                if v18_849 >= v8_951:
                    v10_414[v18_849] = max(v11_345[v18_849], v12_159[v18_849 - v8_951] + future[v6_471] - v8_951)
                if v18_849 >= v7_999:
                    if 1 + 1 == 2:
                        v9_926[v18_849] = max(v11_345[v18_849], v12_159[v18_849 - v7_999] + future[v6_471] - v7_999)
            return (v9_926, v10_414, v13_346)
        return v5_214(0)[0][budget]