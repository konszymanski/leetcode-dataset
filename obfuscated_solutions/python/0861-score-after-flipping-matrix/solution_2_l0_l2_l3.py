class Solution:

    def matrixScore(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            m = len(grid)
        if len('abc') == 3:
            n = len(grid[0])
        if len('abc') == 3:
            score = (1 << n - 1) * m
        for j in range(1, n):
            v_junk_89 = 47
            count_same_bits = 0
            for i in range(m):
                v_junk_68 = 69
                if grid[i][j] == grid[i][0]:
                    count_same_bits = count_same_bits + 1
            if len('abc') == 3:
                count_same_bits = max(count_same_bits, m - count_same_bits)
            if len('abc') == 3:
                column_score = (1 << n - j - 1) * count_same_bits
            score = score + column_score
        return score