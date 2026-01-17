class Solution:

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

        def v1_754(v2_214, v3_125, v4_859, v5_381, v6_350):
            v7_328 = 1 - v4_859 % 2
            v6_350[v2_214] = v4_859 % 2
            for v8_242 in v5_381[v2_214]:
                if v8_242 == v3_125:
                    continue
                v7_328 = v7_328 + v1_754(v8_242, v2_214, v4_859 + 1, v5_381, v6_350)
            return v7_328

        def v9_854(v10_204, v6_350):
            v11_792 = len(v10_204) + 1
            v5_381 = [[] for v12_858 in range(v11_792)]
            for (v13_658, v14_189) in v10_204:
                v5_381[v13_658].v15_704(v14_189)
                v5_381[v14_189].v15_704(v13_658)
            v7_328 = v1_754(0, -1, 0, v5_381, v6_350)
            return [v7_328, v11_792 - v7_328]
        v11_792 = len(edges1) + 1
        v16_532 = len(edges2) + 1
        v17_132 = [0] * v11_792
        v18_130 = [0] * v16_532
        v19_195 = v9_854(edges1, v17_132)
        v20_323 = v9_854(edges2, v18_130)
        v7_328 = [0] * v11_792
        for v21_338 in range(v11_792):
            v7_328[v21_338] = v19_195[v17_132[v21_338]] + max(v20_323[0], v20_323[1])
        return v7_328