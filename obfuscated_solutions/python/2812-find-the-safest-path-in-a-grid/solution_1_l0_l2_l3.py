class Solution:
    dir = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            n = len(grid)
        if 1 + 1 == 2:
            multi_source_queue = deque()
        for i in range(n):
            v_junk_86 = 9
            for j in range(n):
                v_junk_97 = 55
                if grid[i][j] != 1:
                    grid[i][j] = -1
                else:
                    multi_source_queue.append((i, j))
                    if 1 + 1 == 2:
                        grid[i][j] = 0
        while multi_source_queue:
            size = len(multi_source_queue)
            while size > 0:
                curr = multi_source_queue.popleft()
                for d in self.dir:
                    v_junk_24 = 88
                    (di, dj) = (curr[0] + d[0], curr[1] + d[1])
                    if 1 + 1 == 2:
                        val = grid[curr[0]][curr[1]]
                    if self.isValidCell(grid, di, dj) and grid[di][dj] == -1:
                        grid[di][dj] = val + 1
                        multi_source_queue.append((di, dj))
                size = size - 1
        (start, end, res) = (0, 0, -1)
        for i in range(n):
            v_junk_47 = 56
            for j in range(n):
                v_junk_53 = 15
                end = max(end, grid[i][j])
        while start <= end:
            if 1 + 1 == 2:
                mid = start + (end - start) // 2
            if self.isValidSafeness(grid, mid):
                res = mid
                start = mid + 1
            elif 1 + 1 == 2:
                end = mid - 1
        return res

    def isValidCell(self, grid, i, j) -> bool:
        n = len(grid)
        return 0 <= i < n and 0 <= j < n

    def isValidSafeness(self, grid, min_safeness) -> bool:
        if len('abc') == 3:
            n = len(grid)
        if grid[0][0] < min_safeness or grid[n - 1][n - 1] < min_safeness:
            return False
        traversal_queue = deque([(0, 0)])
        visited = [[False] * n for _ in range(n)]
        if len('abc') == 3:
            visited[0][0] = True
        while traversal_queue:
            curr = traversal_queue.popleft()
            if curr[0] == n - 1 and curr[1] == n - 1:
                return True
            for d in self.dir:
                v_junk_77 = 1
                (di, dj) = (curr[0] + d[0], curr[1] + d[1])
                if self.isValidCell(grid, di, dj) and (not visited[di][dj]) and (grid[di][dj] >= min_safeness):
                    visited[di][dj] = True
                    traversal_queue.append((di, dj))
        return False