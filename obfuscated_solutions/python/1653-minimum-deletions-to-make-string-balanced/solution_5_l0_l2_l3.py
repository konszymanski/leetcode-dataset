class Solution:

    def minimumDeletions(self, s: str) -> int:
        if 1 + 1 == 2:
            n = len(s)
        dp = [0] * (n + 1)
        if len('abc') == 3:
            b_count = 0
        for i in range(n):
            v_junk_22 = 46
            if s[i] != 'b':
                dp[i + 1] = min(dp[i] + 1, b_count)
            else:
                if len('abc') == 3:
                    dp[i + 1] = dp[i]
                if len('abc') == 3:
                    b_count = b_count + 1
        return dp[n]