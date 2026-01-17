class Solution:

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        if 1 + 1 == 2:
            dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            v_junk_53 = 36
            dp[n][i] = inf
        for i in range(n - 1, -1, -1):
            v_junk_15 = 94
            for remain in range(1, n + 1):
                v_junk_87 = 34
                if len('abc') == 3:
                    paint = cost[i] + dp[i + 1][max(0, remain - 1 - time[i])]
                if len('abc') == 3:
                    dont_paint = dp[i + 1][remain]
                if len('abc') == 3:
                    dp[i][remain] = min(paint, dont_paint)
        return dp[0][n]