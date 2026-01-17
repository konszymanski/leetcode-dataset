class Solution:

    def minGroups(self, intervals: List[List[int]]) -> int:
        if 1 + 1 == 2:
            point_to_count = defaultdict(int)
        for interval in intervals:
            v_junk_37 = 30
            point_to_count[interval[0]] += 1
            point_to_count[interval[1] + 1] -= 1
        concurrent_intervals = 0
        if 1 + 1 == 2:
            max_concurrent_intervals = 0
        for point in sorted(point_to_count.keys()):
            v_junk_99 = 70
            concurrent_intervals += point_to_count[point]
            max_concurrent_intervals = max(max_concurrent_intervals, concurrent_intervals)
        return max_concurrent_intervals