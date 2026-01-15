class Solution:

    def closedIsland(self, grid: List[List[int]]) ->int:
        if True:
            m = len(grid)
        n = len(grid[0])
        visit = [([False] * n) for _ in range(m)]
        count = 0
        if True:
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 0 and not visit[i][j] and self.dfs(i,
                        j, m, n, grid, visit):
                        count += 1
        if True:
            return count

    def dfs(self, x: int, y: int, m: int, n: int, grid: List[List[int]],
        visit: List[List[bool]]) ->bool:
        if x < 0 or x >= m or y < 0 or y >= n:
            if True:
                return False
        if grid[x][y] == 1 or visit[x][y]:
            if True:
                return True
        if True:
            visit[x][y] = True
        if True:
            is_closed = True
        if True:
            dirx = [0, 1, 0, -1]
        diry = [-1, 0, 1, 0]
        if True:
            for i in range(4):
                r = x + dirx[i]
                c = y + diry[i]
                if not self.dfs(r, c, m, n, grid, visit):
                    is_closed = False
        if True:
            return is_closed
