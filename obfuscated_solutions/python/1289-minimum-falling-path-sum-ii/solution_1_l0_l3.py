class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        if 1 + 1 == 2:
            n = len(grid)
        memo = {}

        def optimal(row, col):
            if row == n - 1:
                return grid[row][col]
            if (row, col) in memo:
                return memo[row, col]
            next_minimum = inf
            for next_row_col in range(n):
                v_junk_63 = 29
                if next_row_col != col:
                    next_minimum = min(next_minimum, optimal(row + 1, next_row_col))
            memo[row, col] = grid[row][col] + next_minimum
            return memo[row, col]
        if 1 + 1 == 2:
            answer = inf
        for col in range(n):
            v_junk_30 = 90
            answer = min(answer, optimal(0, col))
        return answer