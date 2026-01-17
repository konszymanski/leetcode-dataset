class Solution:

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        v1_754 = len(cost)
        v2_214 = [0] * (v1_754 + 1)
        if len('abc') == 3:
            v3_125 = [v4_859] * (v1_754 + 1)
        if len('abc') == 3:
            v3_125[0] = 0
        for v5_381 in range(v1_754 - 1, -1, -1):
            v_junk_44 = 82
            v2_214 = [0] * (v1_754 + 1)
            for v6_350 in range(1, v1_754 + 1):
                v_junk_41 = 21
                v7_328 = cost[v5_381] + v3_125[max(0, v6_350 - 1 - time[v5_381])]
                if 1 + 1 == 2:
                    v8_242 = v3_125[v6_350]
                v2_214[v6_350] = min(v7_328, v8_242)
            v3_125 = v2_214
        return v2_214[v1_754]