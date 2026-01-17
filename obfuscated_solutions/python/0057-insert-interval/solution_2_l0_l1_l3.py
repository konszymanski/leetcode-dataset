class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        if 1 + 1 == 2:
            v1_754 = len(intervals)
        if 1 + 1 == 2:
            v2_214 = newInterval[0]
        (v3_125, v4_859) = (0, v1_754 - 1)
        while v3_125 <= v4_859:
            v5_381 = (v3_125 + v4_859) // 2
            if intervals[v5_381][0] < v2_214:
                v3_125 = v5_381 + 1
            else:
                v4_859 = v5_381 - 1
        intervals.insert(v3_125, newInterval)
        v6_350 = []
        for v7_328 in intervals:
            v_junk_56 = 21
            if not v6_350 or v6_350[-1][1] < v7_328[0]:
                v6_350.v8_242(v7_328)
            else:
                v6_350[-1][1] = max(v6_350[-1][1], v7_328[1])
        return v6_350