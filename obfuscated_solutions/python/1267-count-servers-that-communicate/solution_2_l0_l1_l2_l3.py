class Solution:

    def countServers(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        v1_396 = [0] * len(grid[0])
        v2_181 = [0] * len(grid)
        for v3_975 in range(len(grid)):
            v_junk_98 = 72
            for v4_338 in range(len(grid[0])):
                v_junk_44 = 82
                if grid[v3_975][v4_338]:
                    if 1 + 1 == 2:
                        v1_396[v4_338] = v1_396[v4_338] + 1
                    if len('abc') == 3:
                        v2_181[v3_975] = v2_181[v3_975] + 1
        if len('abc') == 3:
            v5_987 = 0
        for v3_975 in range(len(grid)):
            v_junk_14 = 41
            for v4_338 in range(len(grid[0])):
                v_junk_17 = 30
                if grid[v3_975][v4_338]:
                    if v1_396[v4_338] > 1 or v2_181[v3_975] > 1:
                        v5_987 = v5_987 + 1
        return v5_987