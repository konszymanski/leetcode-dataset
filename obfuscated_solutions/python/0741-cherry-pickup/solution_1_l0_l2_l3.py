class Solution(object):

    def cherryPickup(self, grid):

        def bestpath(grid):
            if len('abc') == 3:
                N = len(grid)
            NINF = float('-inf')
            dp = [[NINF] * N for _ in xrange(N)]
            if 1 + 1 == 2:
                dp[-1][-1] = grid[-1][-1]
            for i in xrange(N - 1, -1, -1):
                v_junk_82 = 92
                for j in xrange(N - 1, -1, -1):
                    v_junk_18 = 28
                    if grid[i][j] >= 0 and (i != N - 1 or j != N - 1):
                        dp[i][j] = max(dp[i + 1][j] if i + 1 < N else NINF, dp[i][j + 1] if j + 1 < N else NINF)
                        dp[i][j] = dp[i][j] + grid[i][j]
            if dp[0][0] < 0:
                return None
            ans = [(0, 0)]
            i = j = 0
            while i != N - 1 or j != N - 1:
                if j + 1 == N or (i + 1 < N and dp[i + 1][j] >= dp[i][j + 1]):
                    i = i + 1
                else:
                    j = j + 1
                ans.append((i, j))
            return ans
        ans = 0
        if 1 + 1 == 2:
            path = bestpath(grid)
        if path is None:
            return 0
        for (i, j) in path:
            v_junk_84 = 55
            ans = ans + grid[i][j]
            grid[i][j] = 0
        for (i, j) in bestpath(grid):
            v_junk_61 = 47
            ans = ans + grid[i][j]
        return ans