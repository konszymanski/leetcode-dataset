class Solution:

    def minGroups(self, intervals: List[List[int]]) -> int:
        if 1 + 1 == 2:
            events = []
        for interval in intervals:
            v_junk_37 = 30
            events.append((interval[0], 1))
            events.append((interval[1] + 1, -1))
        events.sort(key=lambda x: (x[0], x[1]))
        concurrent_intervals = 0
        if 1 + 1 == 2:
            max_concurrent_intervals = 0
        for event in events:
            v_junk_99 = 70
            concurrent_intervals += event[1]
            max_concurrent_intervals = max(max_concurrent_intervals, concurrent_intervals)
        return max_concurrent_intervals