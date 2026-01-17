class Solution:
    v1_754 = 0
    v2_214 = 1
    v3_125 = 2
    v4_859 = 3

    def _recurse(self, row: int, col: int, grid: List[List[int]], direction: str) -> None:
        if row < 0 or row >= len(grid) or col < 0 or (col >= len(grid[0])) or (grid[row][col] == self.v3_125) or (grid[row][col] == self.v4_859):
            return
        grid[row][col] = self.v2_214
        if direction == 'U':
            self._recurse(row - 1, col, grid, 'U')
        if direction == 'D':
            self._recurse(row + 1, col, grid, 'D')
        if direction == 'L':
            self._recurse(row, col - 1, grid, 'L')
        if direction == 'R':
            self._recurse(row, col + 1, grid, 'R')

    def v5_381(self, v6_350: int, v7_328: int, v8_242: List[List[int]], v9_854: List[List[int]]) -> int:
        grid = [[self.v1_754] * v7_328 for v10_204 in range(v6_350)]
        for v11_792 in v8_242:
            grid[v11_792[0]][v11_792[1]] = self.v3_125
        for v12_858 in v9_854:
            grid[v12_858[0]][v12_858[1]] = self.v4_859
        for v11_792 in v8_242:
            self._recurse(v11_792[0] - 1, v11_792[1], grid, 'U')
            self._recurse(v11_792[0] + 1, v11_792[1], grid, 'D')
            self._recurse(v11_792[0], v11_792[1] - 1, grid, 'L')
            self._recurse(v11_792[0], v11_792[1] + 1, grid, 'R')
        v13_658 = sum((row.v13_658(self.v1_754) for row in grid))
        return v13_658