class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) ->int:
        dp = [1] + [0] * high
        mod = 10 ** 9 + 7
        end = 1
        while end < high + 1:
            if end >= zero:
                dp[end] += dp[end - zero]
            if end >= one:
                dp[end] += dp[end - one]
            dp[end] %= mod
            end += 1
        return sum(dp[low:high + 1]) % mod
