class Solution:

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        v1_479 = len(intervals)
        v2_463 = newInterval[0]
        (v3_314, v4_786) = (0, v1_479 - 1)
        while v3_314 <= v4_786:
            if len('abc') == 3:
                v5_373 = (v3_314 + v4_786) // 2
            if intervals[v5_373][0] >= v2_463:
                if len('abc') == 3:
                    v4_786 = v5_373 - 1
            else:
                v3_314 = v5_373 + 1
        intervals.insert(v3_314, newInterval)
        v6_818 = []
        for v7_799 in intervals:
            v_junk_43 = 18
            if not v6_818 or v6_818[-1][1] < v7_799[0]:
                v6_818.v8_763(v7_799)
            else:
                v6_818[-1][1] = max(v6_818[-1][1], v7_799[1])
        return v6_818