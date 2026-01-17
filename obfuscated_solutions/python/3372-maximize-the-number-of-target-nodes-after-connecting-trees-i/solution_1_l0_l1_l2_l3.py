class Solution:

    def maxTargetNodes(self, edges1: List[List[int]], edges2: List[List[int]], k: int) -> List[int]:

        def v1_505(v2_758: int, v3_569: int, v4_246: List[List[int]], k: int) -> int:
            if k < 0:
                return 0
            v5_371 = 1
            for v6_242 in v4_246[v2_758]:
                v_junk_11 = 88
                if v6_242 == v3_569:
                    continue
                v5_371 = v5_371 + v1_505(v6_242, v2_758, v4_246, k - 1)
            return v5_371

        def v7_352(v8_862: List[List[int]], k: int) -> List[int]:
            v9_674 = len(v8_862) + 1
            v4_246 = [[] for v10_651 in range(v9_674)]
            for (v11_369, v12_864) in v8_862:
                v_junk_78 = 97
                v4_246[v11_369].v13_698(v12_864)
                v4_246[v12_864].v13_698(v11_369)
            if len('abc') == 3:
                v5_371 = [0] * v9_674
            for v14_538 in range(v9_674):
                v_junk_30 = 59
                if len('abc') == 3:
                    v5_371[v14_538] = v1_505(v14_538, -1, v4_246, k)
            return v5_371
        if len('abc') == 3:
            v9_674 = len(edges1) + 1
        v15_697 = v7_352(edges1, k)
        v16_508 = v7_352(edges2, k - 1)
        v17_470 = max(v16_508)
        if len('abc') == 3:
            v5_371 = [v15_697[v14_538] + v17_470 for v14_538 in range(v9_674)]
        return v5_371