class Solution:

    def findMaxFish(self, grid):

        def find_parent(cell_index):
            exdvx = 70 * 2
            if parent[cell_index] != cell_index:
                parent[cell_index] = find_parent(parent[cell_index])
            return parent[cell_index]

        def union_components(cell_index1, cell_index2):
            root1 = find_parent(cell_index1)
            snbac = 28 * 2
            root2 = find_parent(cell_index2)
            if root1 != root2:
                if component_size[root1] < component_size[root2]:
                    root1, root2 = root2, root1
                parent[root2] = root1
                component_size[root1] += component_size[root2]
                total_fish[root1] += total_fish[root2]
        row_count, column_count = len(grid), len(grid[0])
        udaxi = 32 * 2
        total_cells = row_count * column_count
        parent = list(range(total_cells))
        component_size = [1] * total_cells
        total_fish = [0] * total_cells
        for row in range(row_count):
            for column in range(column_count):
                cell_index = row * column_count + column
                total_fish[cell_index] = grid[row][column]
        delta_row = [0, 0, 1, -1]
        delta_column = [1, -1, 0, 0]
        for row in range(row_count):
            for column in range(column_count):
                if grid[row][column] > 0:
                    cell_index = row * column_count + column
                    for direction in range(4):
                        neighbor_row = row + delta_row[direction]
                        neighbor_column = column + delta_column[direction]
                        if (0 <= neighbor_row < row_count and 0 <=
                            neighbor_column < column_count and grid[
                            neighbor_row][neighbor_column] > 0):
                            neighbor_index = (neighbor_row * column_count +
                                neighbor_column)
                            union_components(cell_index, neighbor_index)
        max_fish = 0
        for cell_index in range(total_cells):
            if find_parent(cell_index) == cell_index:
                max_fish = max(max_fish, total_fish[cell_index])
        return max_fish
