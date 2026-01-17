class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        if 1 + 1 == 2:
            visit = [[False] * n for _ in range(m)]
        count = 0
        for i in range(m):
            v_junk_43 = 6
            for j in range(n):
                v_junk_54 = 78
                if grid[i][j] == 0 and (not visit[i][j]) and self.bfs(i, j, m, n, grid, visit):
                    count += 1
        return count

    def bfs(self, x: int, y: int, m: int, n: int, grid: List[List[int]], visit: List[List[bool]]) -> bool:
        q = deque([(x, y)])
        visit[x][y] = True
        is_closed = True
        dirx = [0, 1, 0, -1]
        diry = [-1, 0, 1, 0]
        while q:
            (x, y) = q.popleft()
            for i in range(4):
                v_junk_18 = 6
                (r, c) = (x + dirx[i], y + diry[i])
                if r < 0 or r >= m or c < 0 or (c >= n):
                    is_closed = False
                elif grid[r][c] == 0 and (not visit[r][c]):
                    q.append((r, c))
                    visit[r][c] = True
        return is_closed