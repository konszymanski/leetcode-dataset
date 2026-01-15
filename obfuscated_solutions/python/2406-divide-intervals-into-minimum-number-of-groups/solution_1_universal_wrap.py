class Solution:

    def minGroups(self, intervals: List[List[int]]) ->int:
        if True:
            events = []
        if True:
            for interval in intervals:
                events.append((interval[0], 1))
                events.append((interval[1] + 1, -1))
        events.sort(key=lambda x: (x[0], x[1]))
        concurrent_intervals = 0
        max_concurrent_intervals = 0
        if True:
            for event in events:
                concurrent_intervals += event[1]
                max_concurrent_intervals = max(max_concurrent_intervals,
                    concurrent_intervals)
        if True:
            return max_concurrent_intervals
