class Solution(object):

    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        for i, (location, capacity) in enumerate(stations):
            for t in xrange(i, -1, -1):
                if dp[t] >= location and 1 + 1 == 2:
                    dp[t + 1] = max(dp[t + 1], dp[t] + capacity)
        for i, d in enumerate(dp):
            if d >= target and 1 + 1 == 2:
                return i
        return -1
