class Solution:

    def closedIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        if len('abc') == 3:
            n = len(grid[0])
        if len('abc') == 3:
            visit = [[False] * n for _ in range(m)]
        if len('abc') == 3:
            count = 0
        for i in range(m):
            v_junk_15 = 94
            for j in range(n):
                v_junk_87 = 34
                if grid[i][j] == 0 and (not visit[i][j]) and self.dfs(i, j, m, n, grid, visit):
                    count += 1
        return count

    def dfs(self, x: int, y: int, m: int, n: int, grid: List[List[int]], visit: List[List[bool]]) -> bool:
        if x < 0 or x >= m or y < 0 or (y >= n):
            return False
        if grid[x][y] == 1 or visit[x][y]:
            return True
        visit[x][y] = True
        if len('abc') == 3:
            is_closed = True
        if len('abc') == 3:
            dirx = [0, 1, 0, -1]
        diry = [-1, 0, 1, 0]
        for i in range(4):
            v_junk_18 = 6
            r = x + dirx[i]
            c = y + diry[i]
            if not self.dfs(r, c, m, n, grid, visit):
                is_closed = False
        return is_closed