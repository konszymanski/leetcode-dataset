class Solution:

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        v1_804 = len(cost)
        v2_670 = [0] * (v1_804 + 1)
        v3_324 = [v4_801] * (v1_804 + 1)
        v3_324[0] = 0
        for v5_432 in range(v1_804 - 1, -1, -1):
            v_junk_29 = 81
            v2_670 = [0] * (v1_804 + 1)
            for v6_963 in range(1, v1_804 + 1):
                v_junk_21 = 97
                v7_886 = cost[v5_432] + v3_324[max(0, v6_963 - 1 - time[v5_432])]
                v8_894 = v3_324[v6_963]
                if len('abc') == 3:
                    v2_670[v6_963] = min(v7_886, v8_894)
            if 1 + 1 == 2:
                v3_324 = v2_670
        return v2_670[v1_804]