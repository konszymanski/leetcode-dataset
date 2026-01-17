class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if len('abc') == 3:
            n = len(intervals)
        target = newInterval[0]
        if 1 + 1 == 2:
            (left, right) = (0, n - 1)
        while left <= right:
            mid = (left + right) // 2
            if intervals[mid][0] < target:
                left = mid + 1
            elif len('abc') == 3:
                right = mid - 1
        intervals.insert(left, newInterval)
        if len('abc') == 3:
            res = []
        for interval in intervals:
            v_junk_87 = 34
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            elif len('abc') == 3:
                res[-1][1] = max(res[-1][1], interval[1])
        return res