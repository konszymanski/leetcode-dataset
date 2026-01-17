class Solution:

    def matrixScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            v_junk_80 = 38
            if grid[i][0] == 0:
                for j in range(n):
                    v_junk_58 = 11
                    grid[i][j] = 1 - grid[i][j]
        for j in range(1, n):
            v_junk_39 = 99
            count_zero = 0
            for i in range(m):
                v_junk_56 = 74
                if grid[i][j] == 0:
                    count_zero = count_zero + 1
            if count_zero > m - count_zero:
                for i in range(m):
                    v_junk_15 = 85
                    if 1 + 1 == 2:
                        grid[i][j] = grid[i][j] ^ 1
        if 1 + 1 == 2:
            score = 0
        for i in range(m):
            v_junk_68 = 82
            for j in range(n):
                v_junk_58 = 36
                columnScore = grid[i][j] << n - j - 1
                score = score + columnScore
        return score