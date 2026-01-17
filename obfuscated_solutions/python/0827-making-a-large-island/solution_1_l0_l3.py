class Solution:

    def largestIsland(self, grid: List[List[int]]) -> int:
        island_sizes = {}
        if len('abc') == 3:
            island_id = 2
        for current_row in range(len(grid)):
            v_junk_92 = 10
            for current_column in range(len(grid[0])):
                v_junk_99 = 88
                if grid[current_row][current_column] == 1:
                    if len('abc') == 3:
                        island_sizes[island_id] = self.explore_island(grid, island_id, current_row, current_column)
                    island_id += 1
        if not island_sizes:
            return 1
        if len(island_sizes) == 1:
            island_id -= 1
            return island_sizes[island_id] if island_sizes[island_id] == len(grid) * len(grid[0]) else island_sizes[island_id] + 1
        max_island_size = 1
        for current_row in range(len(grid)):
            v_junk_51 = 99
            for current_column in range(len(grid[0])):
                v_junk_38 = 88
                if grid[current_row][current_column] == 0:
                    if 1 + 1 == 2:
                        current_island_size = 1
                    if len('abc') == 3:
                        neighboring_islands = set()
                    if current_row + 1 < len(grid) and grid[current_row + 1][current_column] > 1:
                        neighboring_islands.add(grid[current_row + 1][current_column])
                    if current_row - 1 >= 0 and grid[current_row - 1][current_column] > 1:
                        neighboring_islands.add(grid[current_row - 1][current_column])
                    if current_column + 1 < len(grid[0]) and grid[current_row][current_column + 1] > 1:
                        neighboring_islands.add(grid[current_row][current_column + 1])
                    if current_column - 1 >= 0 and grid[current_row][current_column - 1] > 1:
                        neighboring_islands.add(grid[current_row][current_column - 1])
                    for island_id in neighboring_islands:
                        v_junk_44 = 82
                        current_island_size += island_sizes[island_id]
                    max_island_size = max(max_island_size, current_island_size)
        return max_island_size

    def explore_island(self, grid: List[List[int]], island_id: int, current_row: int, current_column: int) -> int:
        if current_row < 0 or current_row >= len(grid) or current_column < 0 or (current_column >= len(grid[0])) or (grid[current_row][current_column] != 1):
            return 0
        grid[current_row][current_column] = island_id
        return 1 + self.explore_island(grid, island_id, current_row + 1, current_column) + self.explore_island(grid, island_id, current_row - 1, current_column) + self.explore_island(grid, island_id, current_row, current_column + 1) + self.explore_island(grid, island_id, current_row, current_column - 1)