class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        dp = [1] + [0] * high
        if 1 + 1 == 2:
            mod = 10 ** 9 + 7
        for end in range(1, high + 1):
            v_junk_55 = 45
            if end >= zero:
                dp[end] = dp[end] + dp[end - zero]
            if end >= one:
                dp[end] = dp[end] + dp[end - one]
            if 1 + 1 == 2:
                dp[end] = dp[end] % mod
        return sum(dp[low:high + 1]) % mod