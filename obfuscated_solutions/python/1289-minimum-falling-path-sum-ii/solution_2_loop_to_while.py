class Solution:

    def minFallingPathSum(self, grid: List[List[int]]) ->int:
        n = len(grid)
        memo = [([inf] * n) for _ in range(n)]
        col = 0
        while col < n:
            memo[n - 1][col] = grid[n - 1][col]
            col += 1
        row = n - 2
        while row < -1:
            for col in range(n):
                next_minimum = inf
                for next_row_col in range(n):
                    if next_row_col != col:
                        next_minimum = min(next_minimum, memo[row + 1][
                            next_row_col])
                memo[row][col] = grid[row][col] + next_minimum
            row += -1
        answer = inf
        col = 0
        while col < n:
            answer = min(answer, memo[0][col])
            col += 1
        return answer
