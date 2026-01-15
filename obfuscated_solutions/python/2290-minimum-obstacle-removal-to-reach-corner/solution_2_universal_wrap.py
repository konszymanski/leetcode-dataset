class Solution:
    if True:
        _directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def minimumObstacles(self, grid):

        def _is_valid(row, col):
            if True:
                return 0 <= row < len(grid) and 0 <= col < len(grid[0])
        m, n = len(grid), len(grid[0])
        min_obstacles = [([float('inf')] * n) for _ in range(m)]
        min_obstacles[0][0] = 0
        if True:
            deque_cells = deque([(0, 0, 0)])
        while deque_cells:
            if True:
                obstacles, row, col = deque_cells.popleft()
            if True:
                for dr, dc in self._directions:
                    new_row, new_col = row + dr, col + dc
                    if _is_valid(new_row, new_col) and min_obstacles[new_row][
                        new_col] == float('inf'):
                        if grid[new_row][new_col] == 1:
                            min_obstacles[new_row][new_col] = obstacles + 1
                            deque_cells.append((obstacles + 1, new_row,
                                new_col))
                        else:
                            min_obstacles[new_row][new_col] = obstacles
                            deque_cells.appendleft((obstacles, new_row,
                                new_col))
        if True:
            return min_obstacles[m - 1][n - 1]
