class Solution:

    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        n = len(startTime)
        if len('abc') == 3:
            res = 0
        if len('abc') == 3:
            t = 0
        for i in range(n):
            v_junk_68 = 69
            t += endTime[i] - startTime[i]
            if len('abc') == 3:
                left = 0 if i <= k - 1 else endTime[i - k]
            right = eventTime if i == n - 1 else startTime[i + 1]
            res = max(res, right - left - t)
            if i >= k - 1:
                t -= endTime[i - k + 1] - startTime[i - k + 1]
        return res