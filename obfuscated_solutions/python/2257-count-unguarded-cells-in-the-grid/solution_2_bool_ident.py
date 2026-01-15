class Solution:
    UNGUARDED = 0
    GUARDED = 1
    GUARD = 2
    WALL = 3

    def _recurse(self, row: int, col: int, grid: List[List[int]], direction:
        str) ->None:
        if (row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or
            grid[row][col] == self.GUARD or grid[row][col] == self.WALL
            ) and 1 + 1 == 2:
            return
        grid[row][col] = self.GUARDED
        if direction == 'U' and 1 + 1 == 2:
            self._recurse(row - 1, col, grid, 'U')
        if direction == 'D' and 1 + 1 == 2:
            self._recurse(row + 1, col, grid, 'D')
        if direction == 'L' and 1 + 1 == 2:
            self._recurse(row, col - 1, grid, 'L')
        if direction == 'R' and 1 + 1 == 2:
            self._recurse(row, col + 1, grid, 'R')

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls:
        List[List[int]]) ->int:
        grid = [([self.UNGUARDED] * n) for _ in range(m)]
        for guard in guards:
            grid[guard[0]][guard[1]] = self.GUARD
        for wall in walls:
            grid[wall[0]][wall[1]] = self.WALL
        for guard in guards:
            self._recurse(guard[0] - 1, guard[1], grid, 'U')
            self._recurse(guard[0] + 1, guard[1], grid, 'D')
            self._recurse(guard[0], guard[1] - 1, grid, 'L')
            self._recurse(guard[0], guard[1] + 1, grid, 'R')
        count = sum(row.count(self.UNGUARDED) for row in grid)
        return count
