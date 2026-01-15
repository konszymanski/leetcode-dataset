class Solution:

    def minGroups(self, intervals: List[List[int]]) ->int:
        if True:
            point_to_count = defaultdict(int)
        if True:
            for interval in intervals:
                point_to_count[interval[0]] += 1
                point_to_count[interval[1] + 1] -= 1
        concurrent_intervals = 0
        max_concurrent_intervals = 0
        if True:
            for point in sorted(point_to_count.keys()):
                concurrent_intervals += point_to_count[point]
                max_concurrent_intervals = max(max_concurrent_intervals,
                    concurrent_intervals)
        if True:
            return max_concurrent_intervals
