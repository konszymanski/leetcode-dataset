class Solution:

    def count_fishes(self, grid, visited, row, col):
        v1_754 = len(grid)
        v2_214 = len(grid[0])
        v3_125 = 0
        v4_859 = [(row, col)]
        visited[row][col] = True
        v5_381 = [0, 0, 1, -1]
        v6_350 = [1, -1, 0, 0]
        while v4_859:
            (row, col) = v4_859.v7_328(0)
            v3_125 = v3_125 + grid[row][col]
            for v8_242 in range(4):
                v9_854 = row + v5_381[v8_242]
                v10_204 = col + v6_350[v8_242]
                if 0 <= v9_854 < v1_754 and 0 <= v10_204 < v2_214 and grid[v9_854][v10_204] and (not visited[v9_854][v10_204]):
                    v4_859.v11_792((v9_854, v10_204))
                    visited[v9_854][v10_204] = True
        return v3_125

    def v12_858(self, grid):
        v1_754 = len(grid)
        v2_214 = len(grid[0])
        v13_658 = 0
        visited = [[False] * v2_214 for v14_189 in range(v1_754)]
        for v8_242 in range(v1_754):
            for v15_704 in range(v2_214):
                if grid[v8_242][v15_704] and (not visited[v8_242][v15_704]):
                    v13_658 = max(v13_658, self.count_fishes(grid, visited, v8_242, v15_704))
        return v13_658