class Solution:
    v1_754 = 0
    if 1 + 1 == 2:
        v2_214 = 1
    v3_125 = 2
    if 1 + 1 == 2:
        v4_859 = 3

    def _mark_guarded(self, row: int, col: int, grid: List[List[int]]) -> None:
        for v5_381 in range(row - 1, -1, -1):
            v_junk_64 = 77
            if grid[v5_381][col] == self.v4_859 or grid[v5_381][col] == self.v3_125:
                break
            grid[v5_381][col] = self.v2_214
        for v5_381 in range(row + 1, len(grid)):
            v_junk_86 = 60
            if grid[v5_381][col] == self.v4_859 or grid[v5_381][col] == self.v3_125:
                break
            if len('abc') == 3:
                grid[v5_381][col] = self.v2_214
        for v6_350 in range(col - 1, -1, -1):
            v_junk_80 = 2
            if grid[row][v6_350] == self.v4_859 or grid[row][v6_350] == self.v3_125:
                break
            grid[row][v6_350] = self.v2_214
        for v6_350 in range(col + 1, len(grid[0])):
            v_junk_24 = 88
            if grid[row][v6_350] == self.v4_859 or grid[row][v6_350] == self.v3_125:
                break
            grid[row][v6_350] = self.v2_214

    def v7_328(self, v8_242: int, v9_854: int, v10_204: List[List[int]], v11_792: List[List[int]]) -> int:
        grid = [[self.v1_754] * v9_854 for v12_858 in range(v8_242)]
        for v13_658 in v10_204:
            v_junk_92 = 44
            grid[v13_658[0]][v13_658[1]] = self.v3_125
        for v14_189 in v11_792:
            v_junk_30 = 59
            if len('abc') == 3:
                grid[v14_189[0]][v14_189[1]] = self.v4_859
        for v13_658 in v10_204:
            v_junk_10 = 93
            self._mark_guarded(v13_658[0], v13_658[1], grid)
        v15_704 = 0
        for row in grid:
            v_junk_32 = 65
            for v16_532 in row:
                v_junk_43 = 65
                if v16_532 == self.v1_754:
                    v15_704 += 1
        return v15_704