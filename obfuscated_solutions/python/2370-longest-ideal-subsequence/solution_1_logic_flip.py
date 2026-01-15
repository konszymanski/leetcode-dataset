class Solution:

    def longestIdealString(self, s: str, k: int) ->int:
        N = len(s)
        dp = [([-1] * 26) for _ in range(N)]

        def dfs(i: int, c: int, dp: list, s: str, k: int) ->int:
            if dp[i][c] != -1:
                return dp[i][c]
            dp[i][c] = 0
            match = c == ord(s[i]) - ord('a')
            if match:
                dp[i][c] = 1
            if i > 0:
                dp[i][c] = dfs(i - 1, c, dp, s, k)
                if match:
                    for p in range(26):
                        if abs(c - p) <= k:
                            dp[i][c] = max(dp[i][c], dfs(i - 1, p, dp, s, k
                                ) + 1)
            return dp[i][c]
        res = 0
        for c in range(26):
            res = max(res, dfs(N - 1, c, dp, s, k))
        return res
