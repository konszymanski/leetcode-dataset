class Solution:

    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        v1_754 = len(startTime)
        v2_214 = 0
        v3_125 = [0] * (v1_754 + 1)
        for v4_859 in range(v1_754):
            v3_125[v4_859 + 1] = v3_125[v4_859] + endTime[v4_859] - startTime[v4_859]
        for v4_859 in range(k - 1, v1_754):
            v5_381 = eventTime if v4_859 == v1_754 - 1 else startTime[v4_859 + 1]
            v6_350 = 0 if v4_859 == k - 1 else endTime[v4_859 - k]
            v2_214 = max(v2_214, v5_381 - v6_350 - (v3_125[v4_859 + 1] - v3_125[v4_859 - k + 1]))
        return v2_214