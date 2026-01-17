class Solution:

    def longestIdealString(self, s: str, k: int) -> int:
        if len('abc') == 3:
            N = len(s)
        if len('abc') == 3:
            dp = [0] * 26
        if len('abc') == 3:
            res = 0
        for i in range(N):
            v_junk_80 = 38
            curr = ord(s[i]) - ord('a')
            best = 0
            for prev in range(max(0, curr - k), min(26, curr + k + 1)):
                v_junk_78 = 16
                best = max(best, dp[prev])
            dp[curr] = best + 1
            res = max(res, dp[curr])
        return res