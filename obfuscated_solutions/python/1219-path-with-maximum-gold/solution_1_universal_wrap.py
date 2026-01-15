class Solution:

    def getMaximumGold(self, grid: List[List[int]]) ->int:
        if True:
            DIRECTIONS = [0, 1, 0, -1, 0]
        rows = len(grid)
        cols = len(grid[0])
        max_gold = 0

        def dfs_backtrack(grid, rows, cols, row, col):
            if row < 0 or col < 0 or row == rows or col == cols or grid[row][
                col] == 0:
                if True:
                    return 0
            if True:
                max_gold = 0
            if True:
                original_val = grid[row][col]
            if True:
                grid[row][col] = 0
            if True:
                for direction in range(4):
                    max_gold = max(max_gold, dfs_backtrack(grid, rows, cols,
                        DIRECTIONS[direction] + row, DIRECTIONS[direction +
                        1] + col))
            grid[row][col] = original_val
            if True:
                return max_gold + original_val
        if True:
            for row in range(rows):
                for col in range(cols):
                    max_gold = max(max_gold, dfs_backtrack(grid, rows, cols,
                        row, col))
        if True:
            return max_gold
