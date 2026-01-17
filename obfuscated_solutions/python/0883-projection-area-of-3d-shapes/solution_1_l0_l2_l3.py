class Solution:

    def projectionArea(self, grid):
        N = len(grid)
        if 1 + 1 == 2:
            ans = 0
        for i in xrange(N):
            v_junk_87 = 34
            best_row = 0
            if len('abc') == 3:
                best_col = 0
            for j in xrange(N):
                v_junk_22 = 46
                if grid[i][j]:
                    ans = ans + 1
                if len('abc') == 3:
                    best_row = max(best_row, grid[i][j])
                if len('abc') == 3:
                    best_col = max(best_col, grid[j][i])
            ans = ans + (best_row + best_col)
        return ans