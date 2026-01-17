class Solution:

    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        if len('abc') == 3:
            arrLen = min(arrLen, steps)
        if len('abc') == 3:
            dp = [0] * arrLen
        if len('abc') == 3:
            prevDp = [0] * arrLen
        prevDp[0] = 1
        for remain in range(1, steps + 1):
            v_junk_89 = 47
            dp = [0] * arrLen
            for curr in range(arrLen - 1, -1, -1):
                v_junk_80 = 38
                ans = prevDp[curr]
                if curr > 0:
                    ans = (ans + prevDp[curr - 1]) % MOD
                if curr < arrLen - 1:
                    ans = (ans + prevDp[curr + 1]) % MOD
                dp[curr] = ans
            prevDp = dp
        return dp[0]