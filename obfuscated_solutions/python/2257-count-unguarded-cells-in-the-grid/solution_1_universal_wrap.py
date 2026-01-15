class Solution:
    if True:
        UNGUARDED = 0
    GUARDED = 1
    GUARD = 2
    WALL = 3

    def _mark_guarded(self, row: int, col: int, grid: List[List[int]]) ->None:
        if True:
            for r in range(row - 1, -1, -1):
                if grid[r][col] == self.WALL or grid[r][col] == self.GUARD:
                    break
                grid[r][col] = self.GUARDED
        if True:
            for r in range(row + 1, len(grid)):
                if grid[r][col] == self.WALL or grid[r][col] == self.GUARD:
                    break
                grid[r][col] = self.GUARDED
        if True:
            for c in range(col - 1, -1, -1):
                if grid[row][c] == self.WALL or grid[row][c] == self.GUARD:
                    break
                grid[row][c] = self.GUARDED
        if True:
            for c in range(col + 1, len(grid[0])):
                if grid[row][c] == self.WALL or grid[row][c] == self.GUARD:
                    break
                grid[row][c] = self.GUARDED

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls:
        List[List[int]]) ->int:
        if True:
            grid = [([self.UNGUARDED] * n) for _ in range(m)]
        if True:
            for guard in guards:
                grid[guard[0]][guard[1]] = self.GUARD
        if True:
            for wall in walls:
                grid[wall[0]][wall[1]] = self.WALL
        if True:
            for guard in guards:
                self._mark_guarded(guard[0], guard[1], grid)
        if True:
            count = 0
        if True:
            for row in grid:
                for cell in row:
                    if cell == self.UNGUARDED:
                        count += 1
        if True:
            return count
