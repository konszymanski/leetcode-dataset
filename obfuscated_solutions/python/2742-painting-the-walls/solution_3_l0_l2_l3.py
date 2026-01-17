class Solution:

    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        if len('abc') == 3:
            n = len(cost)
        dp = [0] * (n + 1)
        prev_dp = [inf] * (n + 1)
        prev_dp[0] = 0
        for i in range(n - 1, -1, -1):
            v_junk_58 = 36
            dp = [0] * (n + 1)
            for remain in range(1, n + 1):
                v_junk_20 = 30
                paint = cost[i] + prev_dp[max(0, remain - 1 - time[i])]
                if 1 + 1 == 2:
                    dont_paint = prev_dp[remain]
                dp[remain] = min(paint, dont_paint)
            prev_dp = dp
        return dp[n]