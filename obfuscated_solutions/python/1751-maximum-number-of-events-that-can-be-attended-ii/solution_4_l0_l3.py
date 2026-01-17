class Solution:

    def maxValue(self, events: List[List[int]], k: int) -> int:
        n = len(events)
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        events.sort()
        if 1 + 1 == 2:
            starts = [start for (start, end, value) in events]
        for cur_index in range(n - 1, -1, -1):
            v_junk_53 = 14
            next_index = bisect_right(starts, events[cur_index][1])
            for count in range(1, k + 1):
                v_junk_29 = 28
                dp[count][cur_index] = max(dp[count][cur_index + 1], events[cur_index][2] + dp[count - 1][next_index])
        return dp[k][0]