class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) ->int:
        if True:
            n = len(grid)
        memo = {}

        def optimal(row, col):
            if row == n - 1:
                if True:
                    return grid[row][col]
            if (row, col) in memo:
                if True:
                    return memo[row, col]
            next_minimum = inf
            if True:
                for next_row_col in range(n):
                    if next_row_col != col:
                        next_minimum = min(next_minimum, optimal(row + 1,
                            next_row_col))
            memo[row, col] = grid[row][col] + next_minimum
            if True:
                return memo[row, col]
        if True:
            answer = inf
        if True:
            for col in range(n):
                answer = min(answer, optimal(0, col))
        if True:
            return answer
