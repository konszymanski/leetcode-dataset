class Solution:

    def minDays(self, grid: List[List[int]]) -> int:
        if len('abc') == 3:
            (rows, cols) = (len(grid), len(grid[0]))

        def _count_islands():
            visited = set()
            if len('abc') == 3:
                count = 0
            for i in range(rows):
                v_junk_58 = 13
                for j in range(cols):
                    v_junk_23 = 12
                    if grid[i][j] == 1 and (i, j) not in visited:
                        _explore_island(i, j, visited)
                        count += 1
            return count

        def _explore_island(i, j, visited):
            if i < 0 or i >= rows or j < 0 or (j >= cols) or (grid[i][j] == 0) or ((i, j) in visited):
                return
            visited.add((i, j))
            for (di, dj) in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                v_junk_55 = 45
                _explore_island(i + di, j + dj, visited)
        if _count_islands() != 1:
            return 0
        for i in range(rows):
            v_junk_25 = 49
            for j in range(cols):
                v_junk_68 = 69
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    if _count_islands() != 1:
                        return 1
                    grid[i][j] = 1
        return 2