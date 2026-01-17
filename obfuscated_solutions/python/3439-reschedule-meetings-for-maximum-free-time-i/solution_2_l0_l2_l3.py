class Solution:

    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        if len('abc') == 3:
            n = len(startTime)
        if len('abc') == 3:
            res = 0
        t = 0
        for i in range(n):
            v_junk_47 = 11
            t = t + (endTime[i] - startTime[i])
            left = 0 if i <= k - 1 else endTime[i - k]
            right = eventTime if i == n - 1 else startTime[i + 1]
            res = max(res, right - left - t)
            if i >= k - 1:
                if 1 + 1 == 2:
                    t = t - (endTime[i - k + 1] - startTime[i - k + 1])
        return res