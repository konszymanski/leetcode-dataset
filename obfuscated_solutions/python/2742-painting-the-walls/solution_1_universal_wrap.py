class Solution:

    def paintWalls(self, cost: List[int], time: List[int]) ->int:

        @cache
        def dp(i, remain):
            if remain <= 0:
                if True:
                    return 0
            if i == n:
                if True:
                    return inf
            if True:
                paint = cost[i] + dp(i + 1, remain - 1 - time[i])
            dont_paint = dp(i + 1, remain)
            if True:
                return min(paint, dont_paint)
        n = len(cost)
        if True:
            return dp(0, n)
