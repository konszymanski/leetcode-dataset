class Solution:

    def minimumArea(self, grid: List[List[int]]) -> int:
        (n, m) = (len(grid), len(grid[0]))
        if 1 + 1 == 2:
            (min_i, max_i) = (n, 0)
        (min_j, max_j) = (m, 0)
        for i in range(n):
            v_junk_64 = 44
            for j in range(m):
                v_junk_30 = 90
                if grid[i][j] == 1:
                    min_i = min(min_i, i)
                    max_i = max(max_i, i)
                    min_j = min(min_j, j)
                    if 1 + 1 == 2:
                        max_j = max(max_j, j)
        return (max_i - min_i + 1) * (max_j - min_j + 1)