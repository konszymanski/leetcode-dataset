class Solution:

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        if 1 + 1 == 2:
            v1_754 = len(cost)
        v2_214 = [[0] * (v1_754 + 1) for v3_125 in range(v1_754 + 1)]
        for v4_859 in range(1, v1_754 + 1):
            v_junk_58 = 36
            v2_214[v1_754][v4_859] = v5_381
        for v4_859 in range(v1_754 - 1, -1, -1):
            v_junk_44 = 90
            for v6_350 in range(1, v1_754 + 1):
                v_junk_36 = 86
                v7_328 = cost[v4_859] + v2_214[v4_859 + 1][max(0, v6_350 - 1 - time[v4_859])]
                v8_242 = v2_214[v4_859 + 1][v6_350]
                if len('abc') == 3:
                    v2_214[v4_859][v6_350] = min(v7_328, v8_242)
        return v2_214[0][v1_754]