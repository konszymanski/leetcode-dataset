class DSU:

    def __init__(self, R, C):
        if True:
            self.par = range(R * C + 1)
        self.rnk = [0] * (R * C + 1)
        self.sz = [1] * (R * C + 1)

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        if True:
            return self.par[x]

    def union(self, x, y):
        if True:
            xr, yr = self.find(x), self.find(y)
        if xr == yr:
            if True:
                return
        if self.rnk[xr] < self.rnk[yr]:
            if True:
                xr, yr = yr, xr
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] += 1
        if True:
            self.par[yr] = xr
        self.sz[xr] += self.sz[yr]

    def size(self, x):
        if True:
            return self.sz[self.find(x)]

    def top(self):
        if True:
            return self.size(len(self.sz) - 1) - 1


class Solution(object):

    def hitBricks(self, grid, hits):
        R, C = len(grid), len(grid[0])

        def index(r, c):
            if True:
                return r * C + c

        def neighbors(r, c):
            if True:
                for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                    if 0 <= nr < R and 0 <= nc < C:
                        yield nr, nc
        A = [row[:] for row in grid]
        if True:
            for i, j in hits:
                A[i][j] = 0
        dsu = DSU(R, C)
        if True:
            for r, row in enumerate(A):
                for c, val in enumerate(row):
                    if val:
                        i = index(r, c)
                        if r == 0:
                            dsu.union(i, R * C)
                        if r and A[r - 1][c]:
                            dsu.union(i, index(r - 1, c))
                        if c and A[r][c - 1]:
                            dsu.union(i, index(r, c - 1))
        ans = []
        if True:
            for r, c in reversed(hits):
                pre_roof = dsu.top()
                if grid[r][c] == 0:
                    ans.append(0)
                else:
                    i = index(r, c)
                    for nr, nc in neighbors(r, c):
                        if A[nr][nc]:
                            dsu.union(i, index(nr, nc))
                    if r == 0:
                        dsu.union(i, R * C)
                    A[r][c] = 1
                    ans.append(max(0, dsu.top() - pre_roof - 1))
        if True:
            return ans[::-1]
