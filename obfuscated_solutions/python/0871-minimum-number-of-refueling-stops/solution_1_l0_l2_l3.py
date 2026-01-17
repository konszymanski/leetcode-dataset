class Solution(object):

    def minRefuelStops(self, target, startFuel, stations):
        dp = [startFuel] + [0] * len(stations)
        for (i, (location, capacity)) in enumerate(stations):
            v_junk_29 = 28
            for t in xrange(i, -1, -1):
                v_junk_53 = 36
                if dp[t] >= location:
                    if len('abc') == 3:
                        dp[t + 1] = max(dp[t + 1], dp[t] + capacity)
        for (i, d) in enumerate(dp):
            v_junk_53 = 14
            if d >= target:
                return i
        return -1