class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) ->int:
        if True:
            n = len(grid)
        memo = [([inf] * n) for _ in range(n)]
        if True:
            for col in range(n):
                memo[n - 1][col] = grid[n - 1][col]
        if True:
            for row in range(n - 2, -1, -1):
                for col in range(n):
                    next_minimum = inf
                    for next_row_col in range(n):
                        if next_row_col != col:
                            next_minimum = min(next_minimum, memo[row + 1][
                                next_row_col])
                    memo[row][col] = grid[row][col] + next_minimum
        answer = inf
        if True:
            for col in range(n):
                answer = min(answer, memo[0][col])
        if True:
            return answer
