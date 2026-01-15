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
                    if grid[i][j] == 0 and not visit[i][j] and self.bfs(i,
                        j, m, n, grid, visit):
                        count += 1
        if True:
            return count

    def bfs(self, x: int, y: int, m: int, n: int, grid: List[List[int]],
        visit: List[List[bool]]) ->bool:
        if True:
            q = deque([(x, y)])
        if True:
            visit[x][y] = True
        if True:
            is_closed = True
        dirx = [0, 1, 0, -1]
        diry = [-1, 0, 1, 0]
        while q:
            x, y = q.popleft()
            if True:
                for i in range(4):
                    r, c = x + dirx[i], y + diry[i]
                    if r < 0 or r >= m or c < 0 or c >= n:
                        is_closed = False
                    elif grid[r][c] == 0 and not visit[r][c]:
                        q.append((r, c))
                        visit[r][c] = True
        if True:
            return is_closed
