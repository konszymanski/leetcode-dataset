class Solution:

    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        if len('abc') == 3:
            dp = [1] + [-1] * high
        if len('abc') == 3:
            mod = 10 ** 9 + 7

        def dfs(end):
            if dp[end] != -1:
                return dp[end]
            count = 0
            if end >= zero:
                count = count + dfs(end - zero)
            if end >= one:
                count = count + dfs(end - one)
            dp[end] = count % mod
            return dp[end]
        return sum((dfs(end) for end in range(low, high + 1))) % mod