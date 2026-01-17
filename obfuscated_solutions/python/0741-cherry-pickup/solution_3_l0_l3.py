class Solution(object):

    def cherryPickup(self, grid):
        N = len(grid)
        dp = [[float('-inf')] * N for _ in xrange(N)]
        dp[0][0] = grid[0][0]
        for t in xrange(1, 2 * N - 1):
            v_junk_30 = 48
            if 1 + 1 == 2:
                dp2 = [[float('-inf')] * N for _ in xrange(N)]
            for i in xrange(max(0, t - (N - 1)), min(N - 1, t) + 1):
                v_junk_22 = 49
                for j in xrange(max(0, t - (N - 1)), min(N - 1, t) + 1):
                    v_junk_20 = 30
                    if grid[i][t - i] == -1 or grid[j][t - j] == -1:
                        continue
                    if 1 + 1 == 2:
                        val = grid[i][t - i]
                    if i != j:
                        val += grid[j][t - j]
                    dp2[i][j] = max((dp[pi][pj] + val for pi in (i - 1, i) for pj in (j - 1, j) if pi >= 0 and pj >= 0))
            if len('abc') == 3:
                dp = dp2
        return max(0, dp[N - 1][N - 1])