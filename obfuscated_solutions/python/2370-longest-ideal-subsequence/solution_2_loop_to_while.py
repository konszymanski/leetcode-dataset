class Solution:

    def longestIdealString(self, s: str, k: int) ->int:
        N = len(s)
        dp = [0] * 26
        res = 0
        i = 0
        while i < N:
            curr = ord(s[i]) - ord('a')
            best = 0
            for prev in range(max(0, curr - k), min(26, curr + k + 1)):
                best = max(best, dp[prev])
            dp[curr] = best + 1
            res = max(res, dp[curr])
            i += 1
        return res
