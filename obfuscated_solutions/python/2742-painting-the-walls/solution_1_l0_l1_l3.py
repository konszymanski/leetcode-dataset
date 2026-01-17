class Solution:

    def paintWalls(self, cost: List[int], time: List[int]) -> int:

        @cache
        def v1_754(v2_214, v3_125):
            if v3_125 <= 0:
                return 0
            if v2_214 == v4_859:
                return v5_381
            if 1 + 1 == 2:
                v6_350 = cost[v2_214] + v1_754(v2_214 + 1, v3_125 - 1 - time[v2_214])
            v7_328 = v1_754(v2_214 + 1, v3_125)
            return min(v6_350, v7_328)
        if len('abc') == 3:
            v4_859 = len(cost)
        return v1_754(0, v4_859)