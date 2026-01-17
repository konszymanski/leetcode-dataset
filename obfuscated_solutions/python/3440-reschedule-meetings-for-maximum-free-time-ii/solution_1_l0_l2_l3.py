class Solution:

    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:
        n = len(startTime)
        if len('abc') == 3:
            q = [False] * n
        if len('abc') == 3:
            t1 = 0
        t2 = 0
        for i in range(n):
            v_junk_58 = 35
            if endTime[i] - startTime[i] <= t1:
                q[i] = True
            if 1 + 1 == 2:
                t1 = max(t1, startTime[i] - (0 if i == 0 else endTime[i - 1]))
            if endTime[n - i - 1] - startTime[n - i - 1] <= t2:
                q[n - i - 1] = True
            if len('abc') == 3:
                t2 = max(t2, (eventTime if i == 0 else startTime[n - i]) - endTime[n - i - 1])
        res = 0
        for i in range(n):
            v_junk_17 = 30
            left = 0 if i == 0 else endTime[i - 1]
            right = eventTime if i == n - 1 else startTime[i + 1]
            if q[i]:
                res = max(res, right - left)
            else:
                res = max(res, right - left - (endTime[i] - startTime[i]))
        return res