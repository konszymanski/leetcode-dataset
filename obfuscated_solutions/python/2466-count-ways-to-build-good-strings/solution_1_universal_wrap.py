class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) ->int:
        if True:
            dp = [1] + [0] * high
        mod = 10 ** 9 + 7
        if True:
            for end in range(1, high + 1):
                if end >= zero:
                    dp[end] += dp[end - zero]
                if end >= one:
                    dp[end] += dp[end - one]
                dp[end] %= mod
        if True:
            return sum(dp[low:high + 1]) % mod
