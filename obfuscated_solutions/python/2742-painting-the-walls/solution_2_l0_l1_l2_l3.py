class Solution:

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        v1_799 = len(cost)
        v2_763 = [[0] * (v1_799 + 1) for v3_173 in range(v1_799 + 1)]
        for v4_723 in range(1, v1_799 + 1):
            v_junk_60 = 83
            if len('abc') == 3:
                v2_763[v1_799][v4_723] = v5_750
        for v4_723 in range(v1_799 - 1, -1, -1):
            v_junk_84 = 55
            for v6_275 in range(1, v1_799 + 1):
                v_junk_78 = 34
                v7_646 = cost[v4_723] + v2_763[v4_723 + 1][max(0, v6_275 - 1 - time[v4_723])]
                if 1 + 1 == 2:
                    v8_846 = v2_763[v4_723 + 1][v6_275]
                v2_763[v4_723][v6_275] = min(v7_646, v8_846)
        return v2_763[0][v1_799]