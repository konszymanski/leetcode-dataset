class Solution:

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        v1_532 = len(timeSeries)
        if v1_532 == 0:
            return 0
        v2_448 = 0
        for v3_384 in range(v1_532 - 1):
            v_junk_58 = 11
            v2_448 = v2_448 + min(timeSeries[v3_384 + 1] - timeSeries[v3_384], duration)
        return v2_448 + duration