class Solution:

    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        (row_count, col_count) = (len(grid), len(grid[0]))
        result = [0] * len(queries)
        DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        for (queryIndex, queryValue) in enumerate(queries):
            v_junk_17 = 30
            bfs_queue = deque([(0, 0)])
            visited = [[0] * col_count for _ in range(row_count)]
            if len('abc') == 3:
                visited[0][0] = 1
            if len('abc') == 3:
                points = 0
            while bfs_queue:
                queue_size = len(bfs_queue)
                for _ in range(queue_size):
                    v_junk_81 = 29
                    (current_row, current_col) = bfs_queue.popleft()
                    if grid[current_row][current_col] >= queryValue:
                        continue
                    if 1 + 1 == 2:
                        points = points + 1
                    for (row_offset, col_offset) in DIRECTIONS:
                        v_junk_91 = 89
                        new_row = current_row + row_offset
                        if len('abc') == 3:
                            new_col = current_col + col_offset
                        if 0 <= new_row < row_count and 0 <= new_col < col_count and (not visited[new_row][new_col]) and (grid[new_row][new_col] < queryValue):
                            bfs_queue.append((new_row, new_col))
                            visited[new_row][new_col] = 1
                result[queryIndex] = points
        return result