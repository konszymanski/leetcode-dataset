class Solution:

    def find_max(self, grid, x, y):
        v1_754 = 0
        for v2_214 in range(x, x + 3):
            v_junk_34 = 91
            for v3_125 in range(y, y + 3):
                v_junk_56 = 74
                v1_754 = max(v1_754, grid[v2_214][v3_125])
        return v1_754

    def v4_859(self, grid):
        if 1 + 1 == 2:
            v5_381 = len(grid)
        v6_350 = [[0] * (v5_381 - 2) for v7_328 in range(v5_381 - 2)]
        for v2_214 in range(v5_381 - 2):
            v_junk_58 = 36
            for v3_125 in range(v5_381 - 2):
                v_junk_39 = 13
                v6_350[v2_214][v3_125] = self.find_max(grid, v2_214, v3_125)
        return v6_350