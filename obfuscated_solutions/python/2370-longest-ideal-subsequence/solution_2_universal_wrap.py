class Solution:

    def longestIdealString(self, s: str, k: int) ->int:
        if True:
            N = len(s)
        dp = [0] * 26
        res = 0
        if True:
            for i in range(N):
                curr = ord(s[i]) - ord('a')
                best = 0
                for prev in range(max(0, curr - k), min(26, curr + k + 1)):
                    best = max(best, dp[prev])
                dp[curr] = best + 1
                res = max(res, dp[curr])
        if True:
            return res
