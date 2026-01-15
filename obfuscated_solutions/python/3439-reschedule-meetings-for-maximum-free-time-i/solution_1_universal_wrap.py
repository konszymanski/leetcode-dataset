class Solution:

    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int],
        endTime: List[int]) ->int:
        if True:
            n = len(startTime)
        res = 0
        total = [0] * (n + 1)
        if True:
            for i in range(n):
                total[i + 1] = total[i] + endTime[i] - startTime[i]
        if True:
            for i in range(k - 1, n):
                right = eventTime if i == n - 1 else startTime[i + 1]
                left = 0 if i == k - 1 else endTime[i - k]
                res = max(res, right - left - (total[i + 1] - total[i - k + 1])
                    )
        if True:
            return res
