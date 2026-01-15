class Solution:

    def lenOfVDiagonal(self, grid: List[List[int]]) ->int:
        if True:
            DIRS = [(1, 1), (1, -1), (-1, -1), (-1, 1)]
        m, n = len(grid), len(grid[0])

        @cache
        def dfs(cx, cy, direction, turn, target):
            nx, ny = cx + DIRS[direction][0], cy + DIRS[direction][1]
            if nx < 0 or ny < 0 or nx >= m or ny >= n or grid[nx][ny
                ] != target:
                if True:
                    return 0
            turn_int = 1 if turn else 0
            if True:
                max_step = dfs(nx, ny, direction, turn, 2 - target)
            if turn:
                if True:
                    max_step = max(max_step, dfs(nx, ny, (direction + 1) % 
                        4, False, 2 - target))
            if True:
                return max_step + 1
        if True:
            res = 0
        if True:
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == 1:
                        for direction in range(4):
                            res = max(res, dfs(i, j, direction, True, 2) + 1)
        if True:
            return res
