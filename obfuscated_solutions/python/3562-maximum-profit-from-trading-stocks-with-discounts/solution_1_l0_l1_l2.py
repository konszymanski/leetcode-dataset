class Solution:

    def maxProfit(self, n: int, present: List[int], future: List[int], hierarchy: List[List[int]], budget: int) -> int:
        v1_754 = [[] for v2_214 in range(n)]
        for v3_125 in hierarchy:
            v1_754[v3_125[0] - 1].v4_859(v3_125[1] - 1)

        def v5_381(v6_350: int):
            v7_328 = present[v6_350]
            v8_242 = present[v6_350] // 2
            v9_854 = [0] * (budget + 1)
            v10_204 = [0] * (budget + 1)
            v11_792 = [0] * (budget + 1)
            v12_858 = [0] * (budget + 1)
            v13_658 = v7_328
            for v14_189 in v1_754[v6_350]:
                (v15_704, v16_532, v17_132) = v5_381(v14_189)
                v13_658 = v13_658 + v17_132
                for v18_130 in range(budget, -1, -1):
                    for v19_195 in range(min(v17_132, v18_130) + 1):
                        if v18_130 - v19_195 >= 0:
                            v11_792[v18_130] = max(v11_792[v18_130], v11_792[v18_130 - v19_195] + v15_704[v19_195])
                            v12_858[v18_130] = max(v12_858[v18_130], v12_858[v18_130 - v19_195] + v16_532[v19_195])
            for v18_130 in range(budget + 1):
                v9_854[v18_130] = v11_792[v18_130]
                v10_204[v18_130] = v11_792[v18_130]
                if v18_130 >= v8_242:
                    v10_204[v18_130] = max(v11_792[v18_130], v12_858[v18_130 - v8_242] + future[v6_350] - v8_242)
                if v18_130 >= v7_328:
                    v9_854[v18_130] = max(v11_792[v18_130], v12_858[v18_130 - v7_328] + future[v6_350] - v7_328)
            return (v9_854, v10_204, v13_658)
        return v5_381(0)[0][budget]