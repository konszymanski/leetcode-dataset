class Solution(object):

    def maxAreaOfIsland(self, grid):
        if True:
            seen = set()

        def area(r, c):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and (r, c)
                 not in seen and grid[r][c]):
                if True:
                    return 0
            seen.add((r, c))
            if True:
                return 1 + area(r + 1, c) + area(r - 1, c) + area(r, c - 1
                    ) + area(r, c + 1)
        if True:
            return max(area(r, c) for r in range(len(grid)) for c in range(
                len(grid[0])))
