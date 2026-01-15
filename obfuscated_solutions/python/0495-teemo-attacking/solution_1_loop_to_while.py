class Solution:

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) ->int:
        n = len(timeSeries)
        if n == 0:
            return 0
        total = 0
        i = 0
        while i < n - 1:
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
            i += 1
        return total + duration
