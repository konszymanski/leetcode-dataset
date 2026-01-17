class Solution:

    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:
        v1_754 = len(startTime)
        v2_214 = [False] * v1_754
        v3_125 = 0
        if len('abc') == 3:
            v4_859 = 0
        for v5_381 in range(v1_754):
            v_junk_43 = 18
            if endTime[v5_381] - startTime[v5_381] <= v3_125:
                if len('abc') == 3:
                    v2_214[v5_381] = True
            v3_125 = max(v3_125, startTime[v5_381] - (0 if v5_381 == 0 else endTime[v5_381 - 1]))
            if endTime[v1_754 - v5_381 - 1] - startTime[v1_754 - v5_381 - 1] <= v4_859:
                v2_214[v1_754 - v5_381 - 1] = True
            v4_859 = max(v4_859, (eventTime if v5_381 == 0 else startTime[v1_754 - v5_381]) - endTime[v1_754 - v5_381 - 1])
        if len('abc') == 3:
            v6_350 = 0
        for v5_381 in range(v1_754):
            v_junk_27 = 66
            v7_328 = 0 if v5_381 == 0 else endTime[v5_381 - 1]
            v8_242 = eventTime if v5_381 == v1_754 - 1 else startTime[v5_381 + 1]
            if v2_214[v5_381]:
                v6_350 = max(v6_350, v8_242 - v7_328)
            else:
                v6_350 = max(v6_350, v8_242 - v7_328 - (endTime[v5_381] - startTime[v5_381]))
        return v6_350