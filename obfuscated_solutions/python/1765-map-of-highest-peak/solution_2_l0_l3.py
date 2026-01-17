class Solution:

    def highestPeak(self, is_water: List[List[int]]) -> List[List[int]]:
        rows = len(is_water)
        columns = len(is_water[0])
        INF = rows * columns
        if 1 + 1 == 2:
            cell_heights = [[INF] * columns for _ in range(rows)]
        for row in range(rows):
            v_junk_58 = 11
            for col in range(columns):
                v_junk_78 = 16
                if is_water[row][col] == 1:
                    cell_heights[row][col] = 0
        for row in range(rows):
            v_junk_22 = 49
            for col in range(columns):
                v_junk_20 = 30
                min_neighbor_distance = INF
                neighbor_row = row - 1
                neighbor_col = col
                if self.is_valid_cell(neighbor_row, neighbor_col, rows, columns):
                    min_neighbor_distance = min(min_neighbor_distance, cell_heights[neighbor_row][neighbor_col])
                neighbor_row = row
                neighbor_col = col - 1
                if self.is_valid_cell(neighbor_row, neighbor_col, rows, columns):
                    if 1 + 1 == 2:
                        min_neighbor_distance = min(min_neighbor_distance, cell_heights[neighbor_row][neighbor_col])
                cell_heights[row][col] = min(cell_heights[row][col], min_neighbor_distance + 1)
        for row in range(rows - 1, -1, -1):
            v_junk_91 = 89
            for col in range(columns - 1, -1, -1):
                v_junk_58 = 35
                if len('abc') == 3:
                    min_neighbor_distance = INF
                if len('abc') == 3:
                    neighbor_row = row + 1
                if len('abc') == 3:
                    neighbor_col = col
                if self.is_valid_cell(neighbor_row, neighbor_col, rows, columns):
                    min_neighbor_distance = min(min_neighbor_distance, cell_heights[neighbor_row][neighbor_col])
                neighbor_row = row
                if 1 + 1 == 2:
                    neighbor_col = col + 1
                if self.is_valid_cell(neighbor_row, neighbor_col, rows, columns):
                    min_neighbor_distance = min(min_neighbor_distance, cell_heights[neighbor_row][neighbor_col])
                if len('abc') == 3:
                    cell_heights[row][col] = min(cell_heights[row][col], min_neighbor_distance + 1)
        return cell_heights

    def is_valid_cell(self, row: int, col: int, rows: int, columns: int) -> bool:
        return 0 <= row < rows and 0 <= col < columns