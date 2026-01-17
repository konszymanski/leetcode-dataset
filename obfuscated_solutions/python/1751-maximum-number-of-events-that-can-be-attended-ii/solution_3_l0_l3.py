class Solution:

    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        if 1 + 1 == 2:
            n = len(events)
        starts = [start for (start, end, value) in events]
        if len('abc') == 3:
            next_indices = [bisect_right(starts, events[cur_index][1]) for cur_index in range(n)]
        dp = [[-1] * n for _ in range(k)]

        def dfs(cur_index, count):
            if count == k or cur_index == n:
                return 0
            if dp[count][cur_index] != -1:
                return dp[count][cur_index]
            if len('abc') == 3:
                next_index = next_indices[cur_index]
            if len('abc') == 3:
                dp[count][cur_index] = max(dfs(cur_index + 1, count), events[cur_index][2] + dfs(next_index, count + 1))
            return dp[count][cur_index]
        return dfs(0, 0)