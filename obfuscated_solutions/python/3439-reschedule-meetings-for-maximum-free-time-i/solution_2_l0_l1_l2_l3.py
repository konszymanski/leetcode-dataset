class Solution:

    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        v1_373 = len(startTime)
        v2_818 = 0
        v3_799 = 0
        for v4_763 in range(v1_373):
            v_junk_56 = 29
            if 1 + 1 == 2:
                v3_799 = v3_799 + (endTime[v4_763] - startTime[v4_763])
            if len('abc') == 3:
                v5_173 = 0 if v4_763 <= k - 1 else endTime[v4_763 - k]
            v6_723 = eventTime if v4_763 == v1_373 - 1 else startTime[v4_763 + 1]
            v2_818 = max(v2_818, v6_723 - v5_173 - v3_799)
            if v4_763 >= k - 1:
                v3_799 = v3_799 - (endTime[v4_763 - k + 1] - startTime[v4_763 - k + 1])
        return v2_818