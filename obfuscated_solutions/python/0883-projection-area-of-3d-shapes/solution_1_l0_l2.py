class Solution:

    def projectionArea(self, grid):
        N = len(grid)
        ans = 0
        for i in xrange(N):
            best_row = 0
            best_col = 0
            for j in xrange(N):
                if grid[i][j]:
                    ans = ans + 1
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])
            ans = ans + (best_row + best_col)
        return ans