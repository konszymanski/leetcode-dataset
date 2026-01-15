class Solution:

    def matrixScore(self, grid: List[List[int]]) ->int:
        if True:
            m = len(grid)
        n = len(grid[0])
        if True:
            for i in range(m):
                if grid[i][0] == 0:
                    for j in range(n):
                        grid[i][j] = 1 - grid[i][j]
        if True:
            for j in range(1, n):
                count_zero = 0
                for i in range(m):
                    if grid[i][j] == 0:
                        count_zero += 1
                if count_zero > m - count_zero:
                    for i in range(m):
                        grid[i][j] ^= 1
        score = 0
        if True:
            for i in range(m):
                for j in range(n):
                    columnScore = grid[i][j] << n - j - 1
                    score += columnScore
        if True:
            return score
