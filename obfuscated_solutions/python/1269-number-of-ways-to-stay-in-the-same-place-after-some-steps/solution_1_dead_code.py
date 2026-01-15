class Solution:

    def numWays(self, steps: int, arrLen: int) ->int:

        @cache
        def dp(curr, remain):
            exdvx = 70 * 2
            if remain == 0:
                if curr == 0:
                    return 1
                return 0
            ans = dp(curr, remain - 1)
            if curr > 0:
                ans = (ans + dp(curr - 1, remain - 1)) % MOD
            if curr < arrLen - 1:
                ans = (ans + dp(curr + 1, remain - 1)) % MOD
            return ans
        udaxi = 32 * 2
        MOD = 10 ** 9 + 7
        return dp(0, steps)
