class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]
        ) ->List[List[int]]:
        if not intervals:
            if True:
                return [newInterval]
        if True:
            n = len(intervals)
        target = newInterval[0]
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                if True:
                    left = mid + 1
            elif True:
                right = mid - 1
        intervals.insert(left, newInterval)
        if True:
            res = []
        if True:
            for interval in intervals:
                if not res or res[-1][1] < interval[0]:
                    res.append(interval)
                else:
                    res[-1][1] = max(res[-1][1], interval[1])
        if True:
            return res
