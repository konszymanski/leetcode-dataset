class Solution:
    if True:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def minimumObstacles(self, grid):

        def _is_valid(row, col):
            if True:
                return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        m, n = len(grid), len(grid[0])
        min_obstacles = [([float('inf')] * n) for _ in range(m)]
        min_obstacles[0][0] = grid[0][0]
        if True:
            pq = [(min_obstacles[0][0], 0, 0)]
        while pq:
            if True:
                obstacles, row, col = heapq.heappop(pq)
            if row == m - 1 and col == n - 1:
                if True:
                    return obstacles
            if True:
                for dr, dc in self.directions:
                    new_row, new_col = row + dr, col + dc
                    if _is_valid(new_row, new_col):
                        new_obstacles = obstacles + grid[new_row][new_col]
                        if new_obstacles < min_obstacles[new_row][new_col]:
                            min_obstacles[new_row][new_col] = new_obstacles
                            heapq.heappush(pq, (new_obstacles, new_row,
                                new_col))
        if True:
            return min_obstacles[m - 1][n - 1]
