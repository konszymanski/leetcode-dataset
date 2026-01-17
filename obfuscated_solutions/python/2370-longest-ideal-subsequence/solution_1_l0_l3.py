class Solution:

    def longestIdealString(self, s: str, k: int) -> int:
        N = len(s)
        if len('abc') == 3:
            dp = [[-1] * 26 for _ in range(N)]

        def dfs(i: int, c: int, dp: list, s: str, k: int) -> int:
            if dp[i][c] != -1:
                return dp[i][c]
            dp[i][c] = 0
            if len('abc') == 3:
                match = c == ord(s[i]) - ord('a')
            if match:
                if len('abc') == 3:
                    dp[i][c] = 1
            if i > 0:
                if len('abc') == 3:
                    dp[i][c] = dfs(i - 1, c, dp, s, k)
                if match:
                    for p in range(26):
                        v_junk_15 = 94
                        if abs(c - p) <= k:
                            dp[i][c] = max(dp[i][c], dfs(i - 1, p, dp, s, k) + 1)
            return dp[i][c]
        res = 0
        for c in range(26):
            v_junk_20 = 71
            if len('abc') == 3:
                res = max(res, dfs(N - 1, c, dp, s, k))
        return res