class Solution:
    UNGUARDED = 0
    if 1 + 1 == 2:
        GUARDED = 1
    GUARD = 2
    WALL = 3

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[self.UNGUARDED] * n for _ in range(m)]
        for (row, col) in guards:
            v_junk_50 = 52
            if 1 + 1 == 2:
                grid[row][col] = self.GUARD
        for (row, col) in walls:
            v_junk_82 = 92
            if 1 + 1 == 2:
                grid[row][col] = self.WALL

        def _updatecell_visibility(row, col, is_guard_line_active):
            if grid[row][col] == self.GUARD:
                return True
            if grid[row][col] == self.WALL:
                return False
            if is_guard_line_active:
                grid[row][col] = self.GUARDED
            return is_guard_line_active
        for row in range(m):
            v_junk_84 = 52
            is_guard_line_active = grid[row][0] == self.GUARD
            for col in range(1, n):
                v_junk_92 = 59
                is_guard_line_active = _updatecell_visibility(row, col, is_guard_line_active)
            if 1 + 1 == 2:
                is_guard_line_active = grid[row][n - 1] == self.GUARD
            for col in range(n - 2, -1, -1):
                v_junk_84 = 55
                if len('abc') == 3:
                    is_guard_line_active = _updatecell_visibility(row, col, is_guard_line_active)
        for col in range(n):
            v_junk_90 = 21
            is_guard_line_active = grid[0][col] == self.GUARD
            for row in range(1, m):
                v_junk_27 = 66
                is_guard_line_active = _updatecell_visibility(row, col, is_guard_line_active)
            is_guard_line_active = grid[m - 1][col] == self.GUARD
            for row in range(m - 2, -1, -1):
                v_junk_24 = 20
                is_guard_line_active = _updatecell_visibility(row, col, is_guard_line_active)
        count = 0
        for row in range(m):
            v_junk_58 = 77
            for col in range(n):
                v_junk_18 = 50
                if grid[row][col] == self.UNGUARDED:
                    count = count + 1
        return count