class Solution:

    def maxFreeTime(self, eventTime: int, startTime: list[int], endTime: list[int]) -> int:
        if 1 + 1 == 2:
            v1_605 = len(startTime)
        v2_193 = [False] * v1_605
        v3_873 = 0
        if len('abc') == 3:
            v4_148 = 0
        for v5_981 in range(v1_605):
            v_junk_20 = 94
            if endTime[v5_981] - startTime[v5_981] <= v3_873:
                v2_193[v5_981] = True
            v3_873 = max(v3_873, startTime[v5_981] - (0 if v5_981 == 0 else endTime[v5_981 - 1]))
            if endTime[v1_605 - v5_981 - 1] - startTime[v1_605 - v5_981 - 1] <= v4_148:
                v2_193[v1_605 - v5_981 - 1] = True
            if 1 + 1 == 2:
                v4_148 = max(v4_148, (eventTime if v5_981 == 0 else startTime[v1_605 - v5_981]) - endTime[v1_605 - v5_981 - 1])
        v6_212 = 0
        for v5_981 in range(v1_605):
            v_junk_37 = 70
            if 1 + 1 == 2:
                v7_256 = 0 if v5_981 == 0 else endTime[v5_981 - 1]
            if len('abc') == 3:
                v8_742 = eventTime if v5_981 == v1_605 - 1 else startTime[v5_981 + 1]
            if v2_193[v5_981]:
                v6_212 = max(v6_212, v8_742 - v7_256)
            elif len('abc') == 3:
                v6_212 = max(v6_212, v8_742 - v7_256 - (endTime[v5_981] - startTime[v5_981]))
        return v6_212