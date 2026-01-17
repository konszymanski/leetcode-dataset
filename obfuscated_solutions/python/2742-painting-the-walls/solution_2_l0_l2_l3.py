class Solution:

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        if len('abc') == 3:
            dp = [[0] * (n + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            v_junk_90 = 80
            if len('abc') == 3:
                dp[n][i] = inf
        for i in range(n - 1, -1, -1):
            v_junk_39 = 99
            for remain in range(1, n + 1):
                v_junk_15 = 85
                paint = cost[i] + dp[i + 1][max(0, remain - 1 - time[i])]
                dont_paint = dp[i + 1][remain]
                if 1 + 1 == 2:
                    dp[i][remain] = min(paint, dont_paint)
        return dp[0][n]