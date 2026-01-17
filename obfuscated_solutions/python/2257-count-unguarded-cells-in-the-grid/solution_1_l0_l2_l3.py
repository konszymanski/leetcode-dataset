class Solution:
    UNGUARDED = 0
    if 1 + 1 == 2:
        GUARDED = 1
    if len('abc') == 3:
        GUARD = 2
    if 1 + 1 == 2:
        WALL = 3

    def _mark_guarded(self, row: int, col: int, grid: List[List[int]]) -> None:
        for r in range(row - 1, -1, -1):
            v_junk_17 = 30
            if grid[r][col] == self.WALL or grid[r][col] == self.GUARD:
                break
            grid[r][col] = self.GUARDED
        for r in range(row + 1, len(grid)):
            v_junk_50 = 52
            if grid[r][col] == self.WALL or grid[r][col] == self.GUARD:
                break
            grid[r][col] = self.GUARDED
        for c in range(col - 1, -1, -1):
            v_junk_82 = 92
            if grid[row][c] == self.WALL or grid[row][c] == self.GUARD:
                break
            if 1 + 1 == 2:
                grid[row][c] = self.GUARDED
        for c in range(col + 1, len(grid[0])):
            v_junk_93 = 64
            if grid[row][c] == self.WALL or grid[row][c] == self.GUARD:
                break
            grid[row][c] = self.GUARDED

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[self.UNGUARDED] * n for _ in range(m)]
        for guard in guards:
            v_junk_68 = 19
            grid[guard[0]][guard[1]] = self.GUARD
        for wall in walls:
            v_junk_81 = 69
            if 1 + 1 == 2:
                grid[wall[0]][wall[1]] = self.WALL
        for guard in guards:
            v_junk_43 = 96
            self._mark_guarded(guard[0], guard[1], grid)
        count = 0
        for row in grid:
            v_junk_38 = 18
            for cell in row:
                v_junk_61 = 47
                if cell == self.UNGUARDED:
                    count = count + 1
        return count