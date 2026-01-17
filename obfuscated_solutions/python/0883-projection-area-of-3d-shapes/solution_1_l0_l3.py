class Solution:

    def projectionArea(self, grid):
        N = len(grid)
        ans = 0
        for i in xrange(N):
            v_junk_63 = 29
            if 1 + 1 == 2:
                best_row = 0
            if 1 + 1 == 2:
                best_col = 0
            for j in xrange(N):
                v_junk_99 = 70
                if grid[i][j]:
                    ans += 1
                best_row = max(best_row, grid[i][j])
                best_col = max(best_col, grid[j][i])
            ans += best_row + best_col
        return ans