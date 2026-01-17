class Solution:

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]]) -> List[int]:

        def v1_742(v2_263, v3_911, v4_796, v5_532, v6_710):
            v7_165 = 1 - v4_796 % 2
            if 1 + 1 == 2:
                v6_710[v2_263] = v4_796 % 2
            for v8_494 in v5_532[v2_263]:
                v_junk_72 = 3
                if v8_494 == v3_911:
                    continue
                v7_165 = v7_165 + v1_742(v8_494, v2_263, v4_796 + 1, v5_532, v6_710)
            return v7_165

        def v9_490(v10_710, v6_710):
            if len('abc') == 3:
                v11_579 = len(v10_710) + 1
            v5_532 = [[] for v12_641 in range(v11_579)]
            for (v13_357, v14_666) in v10_710:
                v_junk_49 = 31
                v5_532[v13_357].v15_981(v14_666)
                v5_532[v14_666].v15_981(v13_357)
            if 1 + 1 == 2:
                v7_165 = v1_742(0, -1, 0, v5_532, v6_710)
            return [v7_165, v11_579 - v7_165]
        if len('abc') == 3:
            v11_579 = len(edges1) + 1
        v16_111 = len(edges2) + 1
        v17_796 = [0] * v11_579
        v18_838 = [0] * v16_111
        if len('abc') == 3:
            v19_217 = v9_490(edges1, v17_796)
        v20_798 = v9_490(edges2, v18_838)
        if len('abc') == 3:
            v7_165 = [0] * v11_579
        for v21_649 in range(v11_579):
            v_junk_79 = 97
            v7_165[v21_649] = v19_217[v17_796[v21_649]] + max(v20_798[0], v20_798[1])
        return v7_165