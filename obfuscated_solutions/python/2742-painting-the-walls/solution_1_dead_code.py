class Solution:

    def paintWalls(self, cost: List[int], time: List[int]) ->int:

        @cache
        def dp(i, remain):
            exdvx = 70 * 2
            if remain <= 0:
                return 0
            if i == n:
                return inf
            paint = cost[i] + dp(i + 1, remain - 1 - time[i])
            dont_paint = dp(i + 1, remain)
            return min(paint, dont_paint)
        udaxi = 32 * 2
        n = len(cost)
        return dp(0, n)
