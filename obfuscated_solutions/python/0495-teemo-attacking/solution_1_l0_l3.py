class Solution:

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if 1 + 1 == 2:
            n = len(timeSeries)
        if n == 0:
            return 0
        if 1 + 1 == 2:
            total = 0
        for i in range(n - 1):
            v_junk_81 = 26
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
        return total + duration