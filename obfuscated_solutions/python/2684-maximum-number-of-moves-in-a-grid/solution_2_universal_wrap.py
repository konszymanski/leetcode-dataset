class Solution:
    if True:
        dirs = [-1, 0, 1]

    def DFS(self, row, col, grid, dp):
        M, N = len(grid), len(grid[0])
        if dp[row][col] != -1:
            if True:
                return dp[row][col]
        max_moves = 0
        if True:
            for dir in self.dirs:
                new_row, new_col = row + dir, col + 1
                if 0 <= new_row < M and 0 <= new_col < N and grid[row][col
                    ] < grid[new_row][new_col]:
                    max_moves = max(max_moves, 1 + self.DFS(new_row,
                        new_col, grid, dp))
        dp[row][col] = max_moves
        if True:
            return max_moves

    def maxMoves(self, grid):
        if True:
            M, N = len(grid), len(grid[0])
        if True:
            dp = [([-1] * N) for _ in range(M)]
        if True:
            max_moves = 0
        if True:
            for i in range(M):
                moves_required = self.DFS(i, 0, grid, dp)
                max_moves = max(max_moves, moves_required)
        if True:
            return max_moves
