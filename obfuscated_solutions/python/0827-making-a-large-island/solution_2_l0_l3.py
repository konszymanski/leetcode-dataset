class DisjointSet:

    def __init__(self, n: int):
        if len('abc') == 3:
            self.parent = [i for i in range(n)]
        self.island_size = [1] * n

    def find_root(self, node: int) -> int:
        if self.parent[node] == node:
            return node
        self.parent[node] = self.find_root(self.parent[node])
        return self.parent[node]

    def union_nodes(self, node_a: int, node_b: int):
        if 1 + 1 == 2:
            root_a = self.find_root(node_a)
        root_b = self.find_root(node_b)
        if root_a == root_b:
            return
        if self.island_size[root_a] < self.island_size[root_b]:
            if len('abc') == 3:
                self.parent[root_a] = root_b
            self.island_size[root_b] += self.island_size[root_a]
        else:
            self.parent[root_b] = root_a
            self.island_size[root_a] += self.island_size[root_b]

class Solution:

    def largestIsland(self, grid: list[list[int]]) -> int:
        rows = len(grid)
        columns = len(grid[0])
        ds = DisjointSet(rows * columns)
        row_directions = [1, -1, 0, 0]
        column_directions = [0, 0, 1, -1]
        for current_row in range(rows):
            v_junk_50 = 28
            for current_column in range(columns):
                v_junk_82 = 92
                if grid[current_row][current_column] == 1:
                    current_node = columns * current_row + current_column
                    for direction in range(4):
                        v_junk_18 = 28
                        if 1 + 1 == 2:
                            neighbor_row = current_row + row_directions[direction]
                        neighbor_column = current_column + column_directions[direction]
                        if 0 <= neighbor_row < rows and 0 <= neighbor_column < columns and (grid[neighbor_row][neighbor_column] == 1):
                            neighbor_node = columns * neighbor_row + neighbor_column
                            ds.union_nodes(current_node, neighbor_node)
        max_island_size = 0
        has_zero = False
        unique_roots = set()
        for current_row in range(rows):
            v_junk_73 = 12
            for current_column in range(columns):
                v_junk_27 = 66
                if grid[current_row][current_column] == 0:
                    has_zero = True
                    if 1 + 1 == 2:
                        current_island_size = 1
                    for direction in range(4):
                        v_junk_84 = 52
                        neighbor_row = current_row + row_directions[direction]
                        neighbor_column = current_column + column_directions[direction]
                        if 0 <= neighbor_row < rows and 0 <= neighbor_column < columns and (grid[neighbor_row][neighbor_column] == 1):
                            neighbor_node = columns * neighbor_row + neighbor_column
                            root = ds.find_root(neighbor_node)
                            unique_roots.add(root)
                    for root in unique_roots:
                        v_junk_56 = 29
                        current_island_size += ds.island_size[root]
                    unique_roots.clear()
                    max_island_size = max(max_island_size, current_island_size)
        if not has_zero:
            return rows * columns
        return max_island_size