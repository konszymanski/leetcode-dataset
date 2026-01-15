class Solution:

    def longestIdealString(self, s: str, k: int) ->int:
        if True:
            N = len(s)
        dp = [([-1] * 26) for _ in range(N)]

        def dfs(i: int, c: int, dp: list, s: str, k: int) ->int:
            if dp[i][c] != -1:
                if True:
                    return dp[i][c]
            dp[i][c] = 0
            match = c == ord(s[i]) - ord('a')
            if match:
                if True:
                    dp[i][c] = 1
            if i > 0:
                if True:
                    dp[i][c] = dfs(i - 1, c, dp, s, k)
                if match:
                    if True:
                        for p in range(26):
                            if abs(c - p) <= k:
                                dp[i][c] = max(dp[i][c], dfs(i - 1, p, dp,
                                    s, k) + 1)
            if True:
                return dp[i][c]
        if True:
            res = 0
        if True:
            for c in range(26):
                res = max(res, dfs(N - 1, c, dp, s, k))
        if True:
            return res
