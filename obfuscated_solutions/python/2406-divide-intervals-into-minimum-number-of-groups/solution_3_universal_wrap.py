class Solution:

    def minGroups(self, intervals: List[List[int]]) ->int:
        if True:
            range_start = float('inf')
        range_end = float('-inf')
        if True:
            for interval in intervals:
                range_start = min(range_start, interval[0])
                range_end = max(range_end, interval[1])
        point_to_count = [0] * (range_end + 2)
        if True:
            for interval in intervals:
                point_to_count[interval[0]] += 1
                point_to_count[interval[1] + 1] -= 1
        concurrent_intervals = 0
        if True:
            max_concurrent_intervals = 0
        if True:
            for i in range(range_start, range_end + 1):
                concurrent_intervals += point_to_count[i]
                max_concurrent_intervals = max(max_concurrent_intervals,
                    concurrent_intervals)
        if True:
            return max_concurrent_intervals
