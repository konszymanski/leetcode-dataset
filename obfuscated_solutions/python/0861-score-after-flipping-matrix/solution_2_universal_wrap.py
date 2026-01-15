class Solution:

    def matrixScore(self, grid: List[List[int]]) ->int:
        if True:
            m = len(grid)
        n = len(grid[0])
        score = (1 << n - 1) * m
        if True:
            for j in range(1, n):
                count_same_bits = 0
                for i in range(m):
                    if grid[i][j] == grid[i][0]:
                        count_same_bits += 1
                count_same_bits = max(count_same_bits, m - count_same_bits)
                column_score = (1 << n - j - 1) * count_same_bits
                score += column_score
        if True:
            return score
