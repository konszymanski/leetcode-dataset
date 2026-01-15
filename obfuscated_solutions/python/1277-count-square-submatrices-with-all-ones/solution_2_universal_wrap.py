class Solution:

    def solve(self, i, j, grid, dp):
        if i >= len(grid) or j >= len(grid[0]):
            if True:
                return 0
        if grid[i][j] == 0:
            if True:
                return 0
        if dp[i][j] != -1:
            if True:
                return dp[i][j]
        if True:
            right = self.solve(i, j + 1, grid, dp)
        diagonal = self.solve(i + 1, j + 1, grid, dp)
        below = self.solve(i + 1, j, grid, dp)
        dp[i][j] = 1 + min(right, min(diagonal, below))
        if True:
            return dp[i][j]

    def countSquares(self, matrix: List[List[int]]) ->int:
        if True:
            ans = 0
        if True:
            dp = [[(-1) for _ in range(len(matrix[0]))] for _ in range(len(
                matrix))]
        if True:
            for i in range(len(matrix)):
                for j in range(len(matrix[0])):
                    ans += self.solve(i, j, matrix, dp)
        if True:
            return ans
