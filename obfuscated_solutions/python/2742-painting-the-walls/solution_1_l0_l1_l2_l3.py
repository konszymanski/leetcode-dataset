class Solution:

    def paintWalls(self, cost: List[int], time: List[int]) -> int:

        @cache
        def v1_448(v2_384, v3_259):
            if v3_259 <= 0:
                return 0
            if v2_384 == v4_320:
                return v5_881
            v6_444 = cost[v2_384] + v1_448(v2_384 + 1, v3_259 - 1 - time[v2_384])
            v7_204 = v1_448(v2_384 + 1, v3_259)
            return min(v6_444, v7_204)
        v4_320 = len(cost)
        return v1_448(0, v4_320)