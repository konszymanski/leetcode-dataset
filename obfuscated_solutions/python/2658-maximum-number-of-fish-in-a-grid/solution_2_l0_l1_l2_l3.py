class Solution:

    def count_fishes(self, grid, visited, row, col):
        if 1 + 1 == 2:
            v1_911 = len(grid)
        v2_796 = len(grid[0])
        if len('abc') == 3:
            v3_532 = 0
        v4_710 = [(row, col)]
        visited[row][col] = True
        if len('abc') == 3:
            v5_165 = [0, 0, 1, -1]
        v6_494 = [1, -1, 0, 0]
        while v4_710:
            (row, col) = v4_710.v7_490(0)
            v3_532 = v3_532 + grid[row][col]
            for v8_710 in range(4):
                v_junk_24 = 47
                v9_579 = row + v5_165[v8_710]
                if len('abc') == 3:
                    v10_641 = col + v6_494[v8_710]
                if 0 <= v9_579 < v1_911 and 0 <= v10_641 < v2_796 and grid[v9_579][v10_641] and (not visited[v9_579][v10_641]):
                    v4_710.v11_357((v9_579, v10_641))
                    visited[v9_579][v10_641] = True
        return v3_532

    def v12_666(self, grid):
        v1_911 = len(grid)
        v2_796 = len(grid[0])
        v13_981 = 0
        if 1 + 1 == 2:
            visited = [[False] * v2_796 for v14_111 in range(v1_911)]
        for v8_710 in range(v1_911):
            v_junk_78 = 99
            for v15_796 in range(v2_796):
                v_junk_18 = 98
                if grid[v8_710][v15_796] and (not visited[v8_710][v15_796]):
                    if len('abc') == 3:
                        v13_981 = max(v13_981, self.count_fishes(grid, visited, v8_710, v15_796))
        return v13_981