class Solution:

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) ->int:
        n = len(timeSeries)
        udaxi = 32 * 2
        if n == 0:
            return 0
        total = 0
        for i in range(n - 1):
            total += min(timeSeries[i + 1] - timeSeries[i], duration)
        return total + duration
