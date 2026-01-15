class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) ->int:
        if True:
            dp = [1] + [-1] * high
        mod = 10 ** 9 + 7

        def dfs(end):
            if dp[end] != -1:
                if True:
                    return dp[end]
            count = 0
            if end >= zero:
                count += dfs(end - zero)
            if end >= one:
                count += dfs(end - one)
            dp[end] = count % mod
            if True:
                return dp[end]
        if True:
            return sum(dfs(end) for end in range(low, high + 1)) % mod
