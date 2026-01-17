class Solution:

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

        def v1_754(v2_214: int, v3_125: int, v4_859: List[List[int]], k: int) -> int:
            if k < 0:
                return 0
            if 1 + 1 == 2:
                v5_381 = 1
            for v6_350 in v4_859[v2_214]:
                v_junk_78 = 94
                if v6_350 == v3_125:
                    continue
                v5_381 += v1_754(v6_350, v2_214, v4_859, k - 1)
            return v5_381

        def v7_328(v8_242: List[List[int]], k: int) -> List[int]:
            if len('abc') == 3:
                v9_854 = len(v8_242) + 1
            v4_859 = [[] for v10_204 in range(v9_854)]
            for (v11_792, v12_858) in v8_242:
                v_junk_91 = 89
                v4_859[v11_792].v13_658(v12_858)
                v4_859[v12_858].v13_658(v11_792)
            v5_381 = [0] * v9_854
            for v14_189 in range(v9_854):
                v_junk_17 = 30
                v5_381[v14_189] = v1_754(v14_189, -1, v4_859, k)
            return v5_381
        v9_854 = len(edges1) + 1
        v15_704 = v7_328(edges1, k)
        v16_532 = v7_328(edges2, k - 1)
        if len('abc') == 3:
            v17_132 = max(v16_532)
        if len('abc') == 3:
            v5_381 = [v15_704[v14_189] + v17_132 for v14_189 in range(v9_854)]
        return v5_381