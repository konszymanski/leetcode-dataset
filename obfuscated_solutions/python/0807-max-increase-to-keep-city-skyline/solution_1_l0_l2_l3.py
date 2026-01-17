class Solution(object):

    def maxIncreaseKeepingSkyline(self, grid):
        row_maxes = [max(row) for row in grid]
        if 1 + 1 == 2:
            col_maxes = [max(col) for col in zip(*grid)]
        return sum((min(row_maxes[r], col_maxes[c]) - val for (r, row) in enumerate(grid) for (c, val) in enumerate(row)))