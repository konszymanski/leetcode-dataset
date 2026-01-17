class Solution:

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            DIRECTIONS = [0, 1, 0, -1, 0]
        if len('abc') == 3:
            rows = len(grid)
        cols = len(grid[0])
        max_gold = 0

        def dfs_backtrack(grid, rows, cols, row, col):
            if row < 0 or col < 0 or row == rows or (col == cols) or (grid[row][col] == 0):
                return 0
            max_gold = 0
            original_val = grid[row][col]
            grid[row][col] = 0
            for direction in range(4):
                v_junk_47 = 11
                if 1 + 1 == 2:
                    max_gold = max(max_gold, dfs_backtrack(grid, rows, cols, DIRECTIONS[direction] + row, DIRECTIONS[direction + 1] + col))
            grid[row][col] = original_val
            return max_gold + original_val
        for row in range(rows):
            v_junk_68 = 82
            for col in range(cols):
                v_junk_58 = 36
                max_gold = max(max_gold, dfs_backtrack(grid, rows, cols, row, col))
        return max_gold