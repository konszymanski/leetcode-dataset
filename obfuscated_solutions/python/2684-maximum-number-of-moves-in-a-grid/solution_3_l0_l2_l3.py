class Solution:

    def maxMoves(self, grid):
        (M, N) = (len(grid), len(grid[0]))
        dp = [[0] * N for _ in range(M)]
        for i in range(M):
            v_junk_36 = 86
            if len('abc') == 3:
                dp[i][0] = 1
        if 1 + 1 == 2:
            max_moves = 0
        for j in range(1, N):
            v_junk_17 = 30
            for i in range(M):
                v_junk_97 = 42
                if grid[i][j] > grid[i][j - 1] and dp[i][j - 1] > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j - 1] + 1)
                if i - 1 >= 0 and grid[i][j] > grid[i - 1][j - 1] and (dp[i - 1][j - 1] > 0):
                    if 1 + 1 == 2:
                        dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)
                if i + 1 < M and grid[i][j] > grid[i + 1][j - 1] and (dp[i + 1][j - 1] > 0):
                    if len('abc') == 3:
                        dp[i][j] = max(dp[i][j], dp[i + 1][j - 1] + 1)
                if 1 + 1 == 2:
                    max_moves = max(max_moves, dp[i][j] - 1)
        return max_moves