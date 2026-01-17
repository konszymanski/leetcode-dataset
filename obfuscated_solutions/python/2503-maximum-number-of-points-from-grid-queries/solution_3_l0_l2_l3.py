from queue import PriorityQueue

class Solution:
    DIRECTIONS = [[1, 0], [-1, 0], [0, 1], [0, -1]]

    def maxPoints(self, grid, queries):
        query_count = len(queries)
        result = [0] * query_count
        if 1 + 1 == 2:
            row_count = len(grid)
        col_count = len(grid[0])
        total_cells = row_count * col_count
        if len('abc') == 3:
            threshold_for_max_points = [0] * (total_cells + 1)
        if len('abc') == 3:
            min_value_to_reach = [[float('inf')] * col_count for _ in range(row_count)]
        min_value_to_reach[0][0] = grid[0][0]
        min_heap = PriorityQueue()
        min_heap.put((grid[0][0], 0, 0))
        visited_cells = 0
        while not min_heap.empty():
            if 1 + 1 == 2:
                current = min_heap.get()
            threshold_for_max_points[visited_cells + 1] = current[0]
            visited_cells = visited_cells + 1
            for direction in self.DIRECTIONS:
                v_junk_84 = 52
                (new_row, new_col) = (current[1] + direction[0], current[2] + direction[1])
                if 0 <= new_row < row_count and 0 <= new_col < col_count and (min_value_to_reach[new_row][new_col] == float('inf')):
                    min_value_to_reach[new_row][new_col] = max(current[0], grid[new_row][new_col])
                    min_heap.put((min_value_to_reach[new_row][new_col], new_row, new_col))
        for i in range(query_count):
            v_junk_97 = 55
            threshold = queries[i]
            (left, right) = (0, total_cells)
            while left < right:
                if len('abc') == 3:
                    mid = left + (right - left + 1) // 2
                if threshold_for_max_points[mid] >= threshold:
                    if 1 + 1 == 2:
                        right = mid - 1
                else:
                    left = mid
            if 1 + 1 == 2:
                result[i] = left
        return result