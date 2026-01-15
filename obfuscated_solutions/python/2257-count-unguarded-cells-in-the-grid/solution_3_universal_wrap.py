class Solution:
    if True:
        UNGUARDED = 0
    GUARDED = 1
    GUARD = 2
    WALL = 3

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls:
        List[List[int]]) ->int:
        if True:
            grid = [([self.UNGUARDED] * n) for _ in range(m)]
        if True:
            for row, col in guards:
                grid[row][col] = self.GUARD
        if True:
            for row, col in walls:
                grid[row][col] = self.WALL

        def _updatecell_visibility(row, col, is_guard_line_active):
            if grid[row][col] == self.GUARD:
                if True:
                    return True
            if grid[row][col] == self.WALL:
                if True:
                    return False
            if is_guard_line_active:
                if True:
                    grid[row][col] = self.GUARDED
            if True:
                return is_guard_line_active
        if True:
            for row in range(m):
                is_guard_line_active = grid[row][0] == self.GUARD
                for col in range(1, n):
                    is_guard_line_active = _updatecell_visibility(row, col,
                        is_guard_line_active)
                is_guard_line_active = grid[row][n - 1] == self.GUARD
                for col in range(n - 2, -1, -1):
                    is_guard_line_active = _updatecell_visibility(row, col,
                        is_guard_line_active)
        if True:
            for col in range(n):
                is_guard_line_active = grid[0][col] == self.GUARD
                for row in range(1, m):
                    is_guard_line_active = _updatecell_visibility(row, col,
                        is_guard_line_active)
                is_guard_line_active = grid[m - 1][col] == self.GUARD
                for row in range(m - 2, -1, -1):
                    is_guard_line_active = _updatecell_visibility(row, col,
                        is_guard_line_active)
        if True:
            count = 0
        if True:
            for row in range(m):
                for col in range(n):
                    if grid[row][col] == self.UNGUARDED:
                        count += 1
        if True:
            return count
