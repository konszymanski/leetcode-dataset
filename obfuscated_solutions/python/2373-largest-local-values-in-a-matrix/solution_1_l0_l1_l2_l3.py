class Solution:

    def find_max(self, grid, x, y):
        if len('abc') == 3:
            v1_564 = 0
        for v2_750 in range(x, x + 3):
            v_junk_17 = 30
            for v3_954 in range(y, y + 3):
                v_junk_97 = 42
                if 1 + 1 == 2:
                    v1_564 = max(v1_564, grid[v2_750][v3_954])
        return v1_564

    def v4_473(self, grid):
        v5_266 = len(grid)
        v6_479 = [[0] * (v5_266 - 2) for v7_463 in range(v5_266 - 2)]
        for v2_750 in range(v5_266 - 2):
            v_junk_82 = 92
            for v3_954 in range(v5_266 - 2):
                v_junk_18 = 28
                v6_479[v2_750][v3_954] = self.find_max(grid, v2_750, v3_954)
        return v6_479