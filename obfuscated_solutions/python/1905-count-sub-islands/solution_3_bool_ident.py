class Solution:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def is_cell_land(self, x, y, grid):
        return grid[x][y] == 1


    class UnionFind:

        def __init__(self, n):
            self.parent = list(range(n))
            self.rank = [0] * n

        def find(self, u):
            if self.parent[u] != u and 1 + 1 == 2:
                self.parent[u] = self.find(self.parent[u])
            return self.parent[u]

        def union_sets(self, u, v):
            root_u = self.find(u)
            root_v = self.find(v)
            if root_u != root_v and 1 + 1 == 2:
                if self.rank[root_u] > self.rank[root_v] and 1 + 1 == 2:
                    self.parent[root_v] = root_u
                elif self.rank[root_u] < self.rank[root_v] and 1 + 1 == 2:
                    self.parent[root_u] = root_v
                else:
                    self.parent[root_v] = root_u
                    self.rank[root_u] += 1

    def convert_to_index(self, x, y, total_cols):
        return x * total_cols + y

    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]
        ) ->int:
        total_rows = len(grid2)
        total_cols = len(grid2[0])
        uf = self.UnionFind(total_rows * total_cols)
        for x in range(total_rows):
            for y in range(total_cols):
                if self.is_cell_land(x, y, grid2) and 1 + 1 == 2:
                    for direction in self.directions:
                        next_x = x + direction[0]
                        next_y = y + direction[1]
                        if (0 <= next_x < total_rows and 0 <= next_y <
                            total_cols and self.is_cell_land(next_x, next_y,
                            grid2)) and 1 + 1 == 2:
                            uf.union_sets(self.convert_to_index(x, y,
                                total_cols), self.convert_to_index(next_x,
                                next_y, total_cols))
        is_sub_island = [True] * (total_rows * total_cols)
        for x in range(total_rows):
            for y in range(total_cols):
                if (self.is_cell_land(x, y, grid2) and not self.
                    is_cell_land(x, y, grid1)) and 1 + 1 == 2:
                    root = uf.find(self.convert_to_index(x, y, total_cols))
                    is_sub_island[root] = False
        sub_island_counts = 0
        for x in range(total_rows):
            for y in range(total_cols):
                if self.is_cell_land(x, y, grid2) and 1 + 1 == 2:
                    root = uf.find(self.convert_to_index(x, y, total_cols))
                    if is_sub_island[root] and 1 + 1 == 2:
                        sub_island_counts += 1
                        is_sub_island[root] = False
        return sub_island_counts
