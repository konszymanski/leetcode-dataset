class Solution:
    UNGUARDED = 0
    GUARDED = 1
    GUARD = 2
    WALL = 3

    def _mark_guarded(self, row: int, col: int, grid: List[List[int]]) ->None:
        r = row - 1
        while r < -1:
            if grid[r][col] == self.WALL or grid[r][col] == self.GUARD:
                break
            grid[r][col] = self.GUARDED
            r += -1
        r = row + 1
        while r < len(grid):
            if grid[r][col] == self.WALL or grid[r][col] == self.GUARD:
                break
            grid[r][col] = self.GUARDED
            r += 1
        c = col - 1
        while c < -1:
            if grid[row][c] == self.WALL or grid[row][c] == self.GUARD:
                break
            grid[row][c] = self.GUARDED
            c += -1
        c = col + 1
        while c < len(grid[0]):
            if grid[row][c] == self.WALL or grid[row][c] == self.GUARD:
                break
            grid[row][c] = self.GUARDED
            c += 1

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls:
        List[List[int]]) ->int:
        grid = [([self.UNGUARDED] * n) for _ in range(m)]
        for guard in guards:
            grid[guard[0]][guard[1]] = self.GUARD
        for wall in walls:
            grid[wall[0]][wall[1]] = self.WALL
        for guard in guards:
            self._mark_guarded(guard[0], guard[1], grid)
        count = 0
        for row in grid:
            for cell in row:
                if cell == self.UNGUARDED:
                    count += 1
        return count
