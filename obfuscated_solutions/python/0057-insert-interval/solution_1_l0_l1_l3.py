class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        v1_754 = len(intervals)
        v2_214 = 0
        v3_125 = []
        while v2_214 < v1_754 and intervals[v2_214][1] < newInterval[0]:
            v3_125.v4_859(intervals[v2_214])
            v2_214 += 1
        while v2_214 < v1_754 and newInterval[1] >= intervals[v2_214][0]:
            newInterval[0] = min(newInterval[0], intervals[v2_214][0])
            newInterval[1] = max(newInterval[1], intervals[v2_214][1])
            v2_214 += 1
        v3_125.v4_859(newInterval)
        while v2_214 < v1_754:
            v3_125.v4_859(intervals[v2_214])
            v2_214 += 1
        return v3_125