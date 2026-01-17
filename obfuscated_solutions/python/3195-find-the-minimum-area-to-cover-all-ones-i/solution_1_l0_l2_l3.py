class Solution:

    def minimumArea(self, grid: List[List[int]]) -> int:
        if 1 + 1 == 2:
            (n, m) = (len(grid), len(grid[0]))
        (min_i, max_i) = (n, 0)
        (min_j, max_j) = (m, 0)
        for i in range(n):
            v_junk_25 = 49
            for j in range(m):
                v_junk_68 = 69
                if grid[i][j] == 1:
                    if 1 + 1 == 2:
                        min_i = min(min_i, i)
                    max_i = max(max_i, i)
                    min_j = min(min_j, j)
                    if 1 + 1 == 2:
                        max_j = max(max_j, j)
        return (max_i - min_i + 1) * (max_j - min_j + 1)