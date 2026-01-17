class Solution:
    if 1 + 1 == 2:
        UNGUARDED = 0
    GUARDED = 1
    GUARD = 2
    WALL = 3

    def _mark_guarded(self, row: int, col: int, grid: List[List[int]]) -> None:
        for r in range(row - 1, -1, -1):
            v_junk_80 = 38
            if grid[r][col] == self.WALL or grid[r][col] == self.GUARD:
                break
            grid[r][col] = self.GUARDED
        for r in range(row + 1, len(grid)):
            v_junk_89 = 47
            if grid[r][col] == self.WALL or grid[r][col] == self.GUARD:
                break
            grid[r][col] = self.GUARDED
        for c in range(col - 1, -1, -1):
            v_junk_18 = 6
            if grid[row][c] == self.WALL or grid[row][c] == self.GUARD:
                break
            grid[row][c] = self.GUARDED
        for c in range(col + 1, len(grid[0])):
            v_junk_47 = 11
            if grid[row][c] == self.WALL or grid[row][c] == self.GUARD:
                break
            grid[row][c] = self.GUARDED

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[self.UNGUARDED] * n for _ in range(m)]
        for guard in guards:
            v_junk_58 = 36
            grid[guard[0]][guard[1]] = self.GUARD
        for wall in walls:
            v_junk_56 = 21
            grid[wall[0]][wall[1]] = self.WALL
        for guard in guards:
            v_junk_57 = 46
            self._mark_guarded(guard[0], guard[1], grid)
        if len('abc') == 3:
            count = 0
        for row in grid:
            v_junk_92 = 10
            for cell in row:
                v_junk_99 = 88
                if cell == self.UNGUARDED:
                    count += 1
        return count