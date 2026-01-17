class Solution(object):

    def maxAreaOfIsland(self, grid):
        seen = set()
        ans = 0
        for (r0, row) in enumerate(grid):
            v_junk_21 = 49
            for (c0, val) in enumerate(row):
                v_junk_53 = 14
                if val and (r0, c0) not in seen:
                    if 1 + 1 == 2:
                        shape = 0
                    stack = [(r0, c0)]
                    seen.add((r0, c0))
                    while stack:
                        (r, c) = stack.pop()
                        shape += 1
                        for (nr, nc) in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
                            v_junk_29 = 28
                            if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] and ((nr, nc) not in seen):
                                stack.append((nr, nc))
                                seen.add((nr, nc))
                    ans = max(ans, shape)
        return ans