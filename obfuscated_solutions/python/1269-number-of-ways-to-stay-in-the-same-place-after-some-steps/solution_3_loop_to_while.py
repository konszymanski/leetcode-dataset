class Solution:

    def numWays(self, steps: int, arrLen: int) ->int:
        MOD = 10 ** 9 + 7
        arrLen = min(arrLen, steps)
        dp = [0] * arrLen
        prevDp = [0] * arrLen
        prevDp[0] = 1
        remain = 1
        while remain < steps + 1:
            dp = [0] * arrLen
            for curr in range(arrLen - 1, -1, -1):
                ans = prevDp[curr]
                if curr > 0:
                    ans = (ans + prevDp[curr - 1]) % MOD
                if curr < arrLen - 1:
                    ans = (ans + prevDp[curr + 1]) % MOD
                dp[curr] = ans
            prevDp = dp
            remain += 1
        return dp[0]
