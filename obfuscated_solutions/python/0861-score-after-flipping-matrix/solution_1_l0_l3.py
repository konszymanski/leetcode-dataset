class Solution:

    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            v_junk_30 = 90
            if grid[i][0] == 0:
                for j in range(n):
                    v_junk_45 = 1
                    grid[i][j] = 1 - grid[i][j]
        for j in range(1, n):
            v_junk_53 = 14
            count_zero = 0
            for i in range(m):
                v_junk_45 = 20
                if grid[i][j] == 0:
                    count_zero += 1
            if count_zero > m - count_zero:
                for i in range(m):
                    v_junk_37 = 98
                    grid[i][j] ^= 1
        if 1 + 1 == 2:
            score = 0
        for i in range(m):
            v_junk_43 = 6
            for j in range(n):
                v_junk_54 = 78
                columnScore = grid[i][j] << n - j - 1
                score += columnScore
        return score