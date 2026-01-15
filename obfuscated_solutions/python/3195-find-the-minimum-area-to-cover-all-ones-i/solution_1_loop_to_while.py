class Solution:

    def minimumArea(self, grid: List[List[int]]) ->int:
        n, m = len(grid), len(grid[0])
        min_i, max_i = n, 0
        min_j, max_j = m, 0
        i = 0
        while i < n:
            for j in range(m):
                if grid[i][j] == 1:
                    min_i = min(min_i, i)
                    max_i = max(max_i, i)
                    min_j = min(min_j, j)
                    max_j = max(max_j, j)
            i += 1
        return (max_i - min_i + 1) * (max_j - min_j + 1)
