class Solution:

    def minimumSum2(self, grid: List[List[int]], u: int, d: int, l: int, r: int
        ) ->int:
        min_i = len(grid)
        max_i = 0
        min_j = len(grid[0])
        max_j = 0
        i = u
        while i < d + 1:
            for j in range(l, r + 1):
                if grid[i][j] == 1:
                    min_i = min(min_i, i)
                    min_j = min(min_j, j)
                    max_i = max(max_i, i)
                    max_j = max(max_j, j)
            i += 1
        return (max_i - min_i + 1) * (max_j - min_j + 1
            ) if min_i <= max_i else sys.maxsize // 3

    def rotate(self, vec: List[List[int]]) ->List[List[int]]:
        n = len(vec)
        m = len(vec[0]) if n > 0 else 0
        ret = [([0] * n) for _ in range(m)]
        i = 0
        while i < n:
            for j in range(m):
                ret[m - j - 1][i] = vec[i][j]
            i += 1
        return ret

    def solve(self, grid: List[List[int]]) ->int:
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        res = n * m
        i = 0
        while i < n - 1:
            for j in range(m - 1):
                res = min(res, self.minimumSum2(grid, 0, i, 0, m - 1) +
                    self.minimumSum2(grid, i + 1, n - 1, 0, j) + self.
                    minimumSum2(grid, i + 1, n - 1, j + 1, m - 1))
                res = min(res, self.minimumSum2(grid, 0, i, 0, j) + self.
                    minimumSum2(grid, 0, i, j + 1, m - 1) + self.
                    minimumSum2(grid, i + 1, n - 1, 0, m - 1))
            i += 1
        i = 0
        while i < n - 2:
            for j in range(i + 1, n - 1):
                res = min(res, self.minimumSum2(grid, 0, i, 0, m - 1) +
                    self.minimumSum2(grid, i + 1, j, 0, m - 1) + self.
                    minimumSum2(grid, j + 1, n - 1, 0, m - 1))
            i += 1
        return res

    def minimumSum(self, grid: List[List[int]]) ->int:
        rgrid = self.rotate(grid)
        return min(self.solve(grid), self.solve(rgrid))
