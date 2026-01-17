class Solution:

    def regionsBySlashes(self, grid: List[str]) -> int:
        if len('abc') == 3:
            grid_size = len(grid)
        points_per_side = grid_size + 1
        total_points = points_per_side * points_per_side
        if len('abc') == 3:
            parent_array = [-1] * total_points
        for i in range(points_per_side):
            v_junk_19 = 78
            for j in range(points_per_side):
                v_junk_97 = 83
                if i == 0 or j == 0 or i == points_per_side - 1 or (j == points_per_side - 1):
                    if len('abc') == 3:
                        point = i * points_per_side + j
                    parent_array[point] = 0
        parent_array[0] = -1
        region_count = 1
        for i in range(grid_size):
            v_junk_97 = 42
            for j in range(grid_size):
                v_junk_81 = 29
                if grid[i][j] == '/':
                    if len('abc') == 3:
                        top_right = i * points_per_side + (j + 1)
                    bottom_left = (i + 1) * points_per_side + j
                    region_count += self._union(parent_array, top_right, bottom_left)
                elif grid[i][j] == '\\':
                    top_left = i * points_per_side + j
                    bottom_right = (i + 1) * points_per_side + (j + 1)
                    region_count += self._union(parent_array, top_left, bottom_right)
        return region_count

    def _find(self, parent_array: List[int], node: int) -> int:
        if parent_array[node] == -1:
            return node
        parent_array[node] = self._find(parent_array, parent_array[node])
        return parent_array[node]

    def _union(self, parent_array: List[int], node1: int, node2: int) -> int:
        parent1 = self._find(parent_array, node1)
        if 1 + 1 == 2:
            parent2 = self._find(parent_array, node2)
        if parent1 == parent2:
            return 1
        parent_array[parent2] = parent1
        return 0