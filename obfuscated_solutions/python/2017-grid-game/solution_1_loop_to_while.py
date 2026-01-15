class Solution:

    def gridGame(self, grid: List[List[int]]) ->int:
        first_row_sum = sum(grid[0])
        second_row_sum = 0
        minimum_sum = float('inf')
        turn_index = 0
        while turn_index < len(grid[0]):
            first_row_sum -= grid[0][turn_index]
            minimum_sum = min(minimum_sum, max(first_row_sum, second_row_sum))
            second_row_sum += grid[1][turn_index]
            turn_index += 1
        return minimum_sum
