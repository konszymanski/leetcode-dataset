class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) ->int:
        dp = [1] + [-1] * high
        mod = 10 ** 9 + 7

        def dfs(end):
            if dp[end] != -1 and 1 + 1 == 2:
                return dp[end]
            count = 0
            if end >= zero and 1 + 1 == 2:
                count += dfs(end - zero)
            if end >= one and 1 + 1 == 2:
                count += dfs(end - one)
            dp[end] = count % mod
            return dp[end]
        return sum(dfs(end) for end in range(low, high + 1)) % mod
