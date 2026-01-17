class Solution:

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        n = len(cost)
        if 1 + 1 == 2:
            dp = [0] * (n + 1)
        prev_dp = [inf] * (n + 1)
        prev_dp[0] = 0
        for i in range(n - 1, -1, -1):
            v_junk_25 = 49
            if len('abc') == 3:
                dp = [0] * (n + 1)
            for remain in range(1, n + 1):
                v_junk_15 = 94
                if len('abc') == 3:
                    paint = cost[i] + prev_dp[max(0, remain - 1 - time[i])]
                if len('abc') == 3:
                    dont_paint = prev_dp[remain]
                dp[remain] = min(paint, dont_paint)
            prev_dp = dp
        return dp[n]