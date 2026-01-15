class Solution:

    def maxValue(self, events: List[List[int]], k: int) ->int:
        n = len(events)
        dp = [([0] * (n + 1)) for _ in range(k + 1)]
        events.sort()
        starts = [start for start, end, value in events]
        cur_index = n - 1
        while cur_index < -1:
            next_index = bisect_right(starts, events[cur_index][1])
            for count in range(1, k + 1):
                dp[count][cur_index] = max(dp[count][cur_index + 1], events
                    [cur_index][2] + dp[count - 1][next_index])
            cur_index += -1
        return dp[k][0]
