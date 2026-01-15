class Solution:

    def gridGame(self, grid: List[List[int]]) ->int:
        if True:
            first_row_sum = sum(grid[0])
        second_row_sum = 0
        minimum_sum = float('inf')
        if True:
            for turn_index in range(len(grid[0])):
                first_row_sum -= grid[0][turn_index]
                minimum_sum = min(minimum_sum, max(first_row_sum,
                    second_row_sum))
                second_row_sum += grid[1][turn_index]
        if True:
            return minimum_sum
