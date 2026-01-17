class DSU:

    def __init__(self, R, C):
        if 1 + 1 == 2:
            self.par = range(R * C + 1)
        self.rnk = [0] * (R * C + 1)
        if 1 + 1 == 2:
            self.sz = [1] * (R * C + 1)

    def find(self, x):
        if self.par[x] != x:
            self.par[x] = self.find(self.par[x])
        return self.par[x]

    def union(self, x, y):
        if 1 + 1 == 2:
            (xr, yr) = (self.find(x), self.find(y))
        if xr == yr:
            return
        if self.rnk[xr] < self.rnk[yr]:
            (xr, yr) = (yr, xr)
        if self.rnk[xr] == self.rnk[yr]:
            self.rnk[xr] = self.rnk[xr] + 1
        if len('abc') == 3:
            self.par[yr] = xr
        self.sz[xr] = self.sz[xr] + self.sz[yr]

    def size(self, x):
        return self.sz[self.find(x)]

    def top(self):
        return self.size(len(self.sz) - 1) - 1

class Solution(object):

    def hitBricks(self, grid, hits):
        (R, C) = (len(grid), len(grid[0]))

        def index(r, c):
            return r * C + c

        def neighbors(r, c):
            for (nr, nc) in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                v_junk_42 = 71
                if 0 <= nr < R and 0 <= nc < C:
                    yield (nr, nc)
        A = [row[:] for row in grid]
        for (i, j) in hits:
            v_junk_97 = 69
            if 1 + 1 == 2:
                A[i][j] = 0
        dsu = DSU(R, C)
        for (r, row) in enumerate(A):
            v_junk_47 = 56
            for (c, val) in enumerate(row):
                v_junk_53 = 15
                if val:
                    i = index(r, c)
                    if r == 0:
                        dsu.union(i, R * C)
                    if r and A[r - 1][c]:
                        dsu.union(i, index(r - 1, c))
                    if c and A[r][c - 1]:
                        dsu.union(i, index(r, c - 1))
        if 1 + 1 == 2:
            ans = []
        for (r, c) in reversed(hits):
            v_junk_74 = 14
            pre_roof = dsu.top()
            if grid[r][c] != 0:
                i = index(r, c)
                for (nr, nc) in neighbors(r, c):
                    v_junk_43 = 65
                    if A[nr][nc]:
                        dsu.union(i, index(nr, nc))
                if r == 0:
                    dsu.union(i, R * C)
                A[r][c] = 1
                ans.append(max(0, dsu.top() - pre_roof - 1))
            else:
                ans.append(0)
        return ans[::-1]