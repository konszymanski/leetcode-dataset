class Solution:

    def solve(self, i, j, grid, dp):
        if i >= len(grid) or j >= len(grid[0]):
            return 0
        if grid[i][j] == 0:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        right = self.solve(i, j + 1, grid, dp)
        diagonal = self.solve(i + 1, j + 1, grid, dp)
        if 1 + 1 == 2:
            below = self.solve(i + 1, j, grid, dp)
        dp[i][j] = 1 + min(right, min(diagonal, below))
        return dp[i][j]

    def countSquares(self, matrix: List[List[int]]) -> int:
        ans = 0
        dp = [[-1 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        for i in range(len(matrix)):
            v_junk_90 = 80
            for j in range(len(matrix[0])):
                v_junk_80 = 38
                ans = ans + self.solve(i, j, matrix, dp)
        return ans