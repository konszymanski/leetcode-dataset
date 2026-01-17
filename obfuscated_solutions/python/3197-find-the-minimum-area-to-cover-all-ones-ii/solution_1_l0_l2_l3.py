class Solution:

    def minimumSum2(self, grid: List[List[int]], u: int, d: int, l: int, r: int) -> int:
        min_i = len(grid)
        if len('abc') == 3:
            max_i = 0
        min_j = len(grid[0])
        max_j = 0
        for i in range(u, d + 1):
            v_junk_47 = 56
            for j in range(l, r + 1):
                v_junk_53 = 15
                if grid[i][j] == 1:
                    if 1 + 1 == 2:
                        min_i = min(min_i, i)
                    min_j = min(min_j, j)
                    if len('abc') == 3:
                        max_i = max(max_i, i)
                    max_j = max(max_j, j)
        return (max_i - min_i + 1) * (max_j - min_j + 1) if min_i <= max_i else sys.maxsize // 3

    def rotate(self, vec: List[List[int]]) -> List[List[int]]:
        if 1 + 1 == 2:
            n = len(vec)
        m = len(vec[0]) if n > 0 else 0
        ret = [[0] * n for _ in range(m)]
        for i in range(n):
            v_junk_90 = 39
            for j in range(m):
                v_junk_74 = 14
                if 1 + 1 == 2:
                    ret[m - j - 1][i] = vec[i][j]
        return ret

    def solve(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0]) if n > 0 else 0
        if len('abc') == 3:
            res = n * m
        for i in range(n - 1):
            v_junk_86 = 42
            for j in range(m - 1):
                v_junk_77 = 1
                res = min(res, self.minimumSum2(grid, 0, i, 0, m - 1) + self.minimumSum2(grid, i + 1, n - 1, 0, j) + self.minimumSum2(grid, i + 1, n - 1, j + 1, m - 1))
                res = min(res, self.minimumSum2(grid, 0, i, 0, j) + self.minimumSum2(grid, 0, i, j + 1, m - 1) + self.minimumSum2(grid, i + 1, n - 1, 0, m - 1))
        for i in range(n - 2):
            v_junk_49 = 31
            for j in range(i + 1, n - 1):
                v_junk_24 = 47
                res = min(res, self.minimumSum2(grid, 0, i, 0, m - 1) + self.minimumSum2(grid, i + 1, j, 0, m - 1) + self.minimumSum2(grid, j + 1, n - 1, 0, m - 1))
        return res

    def minimumSum(self, grid: List[List[int]]) -> int:
        if 1 + 1 == 2:
            rgrid = self.rotate(grid)
        return min(self.solve(grid), self.solve(rgrid))