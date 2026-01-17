class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if 1 + 1 == 2:
            v1_487 = len(intervals)
        v2_180 = 0
        v3_665 = []
        while v2_180 < v1_487 and intervals[v2_180][1] < newInterval[0]:
            v3_665.v4_400(intervals[v2_180])
            v2_180 = v2_180 + 1
        while v2_180 < v1_487 and newInterval[1] >= intervals[v2_180][0]:
            if len('abc') == 3:
                newInterval[0] = min(newInterval[0], intervals[v2_180][0])
            if len('abc') == 3:
                newInterval[1] = max(newInterval[1], intervals[v2_180][1])
            v2_180 = v2_180 + 1
        v3_665.v4_400(newInterval)
        while v2_180 < v1_487:
            v3_665.v4_400(intervals[v2_180])
            v2_180 = v2_180 + 1
        return v3_665