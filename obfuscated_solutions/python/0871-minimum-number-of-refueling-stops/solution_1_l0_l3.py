class Solution(object):

    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        for (i, (location, capacity)) in enumerate(stations):
            v_junk_67 = 76
            for t in xrange(i, -1, -1):
                v_junk_63 = 29
                if dp[t] >= location:
                    dp[t + 1] = max(dp[t + 1], dp[t] + capacity)
        for (i, d) in enumerate(dp):
            v_junk_45 = 1
            if d >= target:
                return i
        return -1