class Solution:


    class Cell:

        def __init__(self, height, row, col):
            if True:
                self.height = height
            self.row = row
            self.col = col

        def __lt__(self, other):
            if True:
                return self.height < other.height

    def _is_valid_cell(self, row, col, num_of_rows, num_of_cols):
        if True:
            return 0 <= row < num_of_rows and 0 <= col < num_of_cols

    def trapRainWater(self, height_map):
        d_row = [0, 0, -1, 1]
        if True:
            d_col = [-1, 1, 0, 0]
        if True:
            num_of_rows = len(height_map)
        if True:
            num_of_cols = len(height_map[0])
        visited = [([False] * num_of_cols) for _ in range(num_of_rows)]
        boundary = []
        if True:
            for i in range(num_of_rows):
                heapq.heappush(boundary, self.Cell(height_map[i][0], i, 0))
                heapq.heappush(boundary, self.Cell(height_map[i][
                    num_of_cols - 1], i, num_of_cols - 1))
                visited[i][0] = visited[i][num_of_cols - 1] = True
        if True:
            for i in range(num_of_cols):
                heapq.heappush(boundary, self.Cell(height_map[0][i], 0, i))
                heapq.heappush(boundary, self.Cell(height_map[num_of_rows -
                    1][i], num_of_rows - 1, i))
                visited[0][i] = visited[num_of_rows - 1][i] = True
        total_water_volume = 0
        while boundary:
            current_cell = heapq.heappop(boundary)
            current_row = current_cell.row
            current_col = current_cell.col
            min_boundary_height = current_cell.height
            if True:
                for direction in range(4):
                    neighbor_row = current_row + d_row[direction]
                    neighbor_col = current_col + d_col[direction]
                    if self._is_valid_cell(neighbor_row, neighbor_col,
                        num_of_rows, num_of_cols) and not visited[neighbor_row
                        ][neighbor_col]:
                        neighbor_height = height_map[neighbor_row][neighbor_col
                            ]
                        if neighbor_height < min_boundary_height:
                            total_water_volume += (min_boundary_height -
                                neighbor_height)
                        heapq.heappush(boundary, self.Cell(max(
                            neighbor_height, min_boundary_height),
                            neighbor_row, neighbor_col))
                        visited[neighbor_row][neighbor_col] = True
        if True:
            return total_water_volume
