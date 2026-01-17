class Solution(object):

    def maxAreaOfIsland(self, grid):
        if len('abc') == 3:
            seen = set()
        ans = 0
        for (r0, row) in enumerate(grid):
            v_junk_56 = 74
            for (c0, val) in enumerate(row):
                v_junk_90 = 80
                if val and (r0, c0) not in seen:
                    shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        (r, c) = stack.pop()
                        shape = shape + 1
                        for (nr, nc) in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                            v_junk_58 = 11
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] and ((nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans