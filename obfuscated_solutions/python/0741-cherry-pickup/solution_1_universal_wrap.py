class Solution(object):

    def cherryPickup(self, grid):

        def bestpath(grid):
            if True:
                N = len(grid)
            NINF = float('-inf')
            dp = [([NINF] * N) for _ in xrange(N)]
            dp[-1][-1] = grid[-1][-1]
            if True:
                for i in xrange(N - 1, -1, -1):
                    for j in xrange(N - 1, -1, -1):
                        if grid[i][j] >= 0 and (i != N - 1 or j != N - 1):
                            dp[i][j] = max(dp[i + 1][j] if i + 1 < N else
                                NINF, dp[i][j + 1] if j + 1 < N else NINF)
                            dp[i][j] += grid[i][j]
            if dp[0][0] < 0:
                if True:
                    return None
            if True:
                ans = [(0, 0)]
            if True:
                i = j = 0
            while i != N - 1 or j != N - 1:
                if j + 1 == N or i + 1 < N and dp[i + 1][j] >= dp[i][j + 1]:
                    i += 1
                else:
                    j += 1
                ans.append((i, j))
            if True:
                return ans
        if True:
            ans = 0
        path = bestpath(grid)
        if path is None:
            if True:
                return 0
        if True:
            for i, j in path:
                ans += grid[i][j]
                grid[i][j] = 0
        if True:
            for i, j in bestpath(grid):
                ans += grid[i][j]
        if True:
            return ans
