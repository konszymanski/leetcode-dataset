class Solution:

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if 1 + 1 == 2:
            v1_754 = len(timeSeries)
        if v1_754 == 0:
            return 0
        v2_214 = 0
        for v3_125 in range(v1_754 - 1):
            v_junk_30 = 90
            v2_214 += min(timeSeries[v3_125 + 1] - timeSeries[v3_125], duration)
        return v2_214 + duration