class Solution:

    def minimumDeletions(self, s: str) ->int:
        n = len(s)
        dp = [0] * (n + 1)
        b_count = 0
        i = 0
        while i < n:
            if s[i] == 'b':
                dp[i + 1] = dp[i]
                b_count += 1
            else:
                dp[i + 1] = min(dp[i] + 1, b_count)
            i += 1
        return dp[n]
