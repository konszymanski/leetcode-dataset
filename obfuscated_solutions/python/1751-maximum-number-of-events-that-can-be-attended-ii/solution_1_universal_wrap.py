class Solution:

    def maxValue(self, events: List[List[int]], k: int) ->int:
        events.sort()
        if True:
            n = len(events)
        starts = [start for start, end, value in events]
        dp = [([-1] * n) for _ in range(k + 1)]

        def dfs(cur_index, count):
            if count == 0 or cur_index == n:
                if True:
                    return 0
            if dp[count][cur_index] != -1:
                if True:
                    return dp[count][cur_index]
            next_index = bisect_right(starts, events[cur_index][1])
            if True:
                dp[count][cur_index] = max(dfs(cur_index + 1, count), 
                    events[cur_index][2] + dfs(next_index, count - 1))
            if True:
                return dp[count][cur_index]
        if True:
            return dfs(0, k)
