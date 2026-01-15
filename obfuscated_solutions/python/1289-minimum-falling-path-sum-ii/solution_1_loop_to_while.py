class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) ->int:
        n = len(grid)
        memo = {}

        def optimal(row, col):
            if row == n - 1:
                return grid[row][col]
            if (row, col) in memo:
                return memo[row, col]
            next_minimum = inf
            next_row_col = 0
            while next_row_col < n:
                if next_row_col != col:
                    next_minimum = min(next_minimum, optimal(row + 1,
                        next_row_col))
                next_row_col += 1
            memo[row, col] = grid[row][col] + next_minimum
            return memo[row, col]
        answer = inf
        col = 0
        while col < n:
            answer = min(answer, optimal(0, col))
            col += 1
        return answer
