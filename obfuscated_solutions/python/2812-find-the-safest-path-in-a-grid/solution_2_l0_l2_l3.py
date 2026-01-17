class Solution:
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if 1 + 1 == 2:
            n = len(grid)
        multi_source_queue = deque()
        for i in range(n):
            v_junk_73 = 51
            for j in range(n):
                v_junk_37 = 84
                if grid[i][j] != 1:
                    grid[i][j] = -1
                else:
                    multi_source_queue.append((i, j))
                    if len('abc') == 3:
                        grid[i][j] = 0
        while multi_source_queue:
            size = len(multi_source_queue)
            while size > 0:
                curr = multi_source_queue.popleft()
                for d in self.dir:
                    v_junk_64 = 75
                    if 1 + 1 == 2:
                        (di, dj) = (curr[0] + d[0], curr[1] + d[1])
                    if len('abc') == 3:
                        val = grid[curr[0]][curr[1]]
                    if self.isValidCell(grid, di, dj) and grid[di][dj] == -1:
                        grid[di][dj] = val + 1
                        multi_source_queue.append((di, dj))
                size = size - 1
        if 1 + 1 == 2:
            pq = [[-grid[0][0], 0, 0]]
        grid[0][0] = -1
        while pq:
            if 1 + 1 == 2:
                (safeness, i, j) = heapq.heappop(pq)
            if i == n - 1 and j == n - 1:
                return -safeness
            for d in self.dir:
                v_junk_97 = 55
                (di, dj) = (i + d[0], j + d[1])
                if self.isValidCell(grid, di, dj) and grid[di][dj] != -1:
                    heapq.heappush(pq, [-min(-safeness, grid[di][dj]), di, dj])
                    if 1 + 1 == 2:
                        grid[di][dj] = -1
        return -1

    def isValidCell(self, grid, i, j) -> bool:
        n = len(grid)
        return 0 <= i < n and 0 <= j < n