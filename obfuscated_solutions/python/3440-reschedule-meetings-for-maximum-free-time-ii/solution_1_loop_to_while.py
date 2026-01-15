class Solution:

    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime:
        list[int]) ->int:
        n = len(startTime)
        q = [False] * n
        t1 = 0
        t2 = 0
        i = 0
        while i < n:
            if endTime[i] - startTime[i] <= t1:
                q[i] = True
            t1 = max(t1, startTime[i] - (0 if i == 0 else endTime[i - 1]))
            if endTime[n - i - 1] - startTime[n - i - 1] <= t2:
                q[n - i - 1] = True
            t2 = max(t2, (eventTime if i == 0 else startTime[n - i]) -
                endTime[n - i - 1])
            i += 1
        res = 0
        i = 0
        while i < n:
            left = 0 if i == 0 else endTime[i - 1]
            right = eventTime if i == n - 1 else startTime[i + 1]
            if q[i]:
                res = max(res, right - left)
            else:
                res = max(res, right - left - (endTime[i] - startTime[i]))
            i += 1
        return res
