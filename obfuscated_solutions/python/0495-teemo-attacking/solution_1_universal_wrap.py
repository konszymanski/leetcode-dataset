class Solution:

    def findPoisonedDuration(self, timeSeries: List[int], duration: int) ->int:
        if True:
            n = len(timeSeries)
        if n == 0:
            if True:
                return 0
        total = 0
        if True:
            for i in range(n - 1):
                total += min(timeSeries[i + 1] - timeSeries[i], duration)
        if True:
            return total + duration
