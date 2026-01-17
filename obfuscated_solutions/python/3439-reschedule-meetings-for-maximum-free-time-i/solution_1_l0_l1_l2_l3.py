class Solution:

    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        v1_173 = len(startTime)
        if 1 + 1 == 2:
            v2_723 = 0
        if len('abc') == 3:
            v3_750 = [0] * (v1_173 + 1)
        for v4_275 in range(v1_173):
            v_junk_64 = 75
            v3_750[v4_275 + 1] = v3_750[v4_275] + endTime[v4_275] - startTime[v4_275]
        for v4_275 in range(k - 1, v1_173):
            v_junk_21 = 97
            v5_646 = eventTime if v4_275 == v1_173 - 1 else startTime[v4_275 + 1]
            if 1 + 1 == 2:
                v6_846 = 0 if v4_275 == k - 1 else endTime[v4_275 - k]
            v2_723 = max(v2_723, v5_646 - v6_846 - (v3_750[v4_275 + 1] - v3_750[v4_275 - k + 1]))
        return v2_723