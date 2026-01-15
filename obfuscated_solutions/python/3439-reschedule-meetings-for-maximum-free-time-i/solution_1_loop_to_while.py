class Solution:

    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int],
        endTime: List[int]) ->int:
        n = len(startTime)
        res = 0
        total = [0] * (n + 1)
        i = 0
        while i < n:
            total[i + 1] = total[i] + endTime[i] - startTime[i]
            i += 1
        i = k - 1
        while i < n:
            right = eventTime if i == n - 1 else startTime[i + 1]
            left = 0 if i == k - 1 else endTime[i - k]
            res = max(res, right - left - (total[i + 1] - total[i - k + 1]))
            i += 1
        return res
