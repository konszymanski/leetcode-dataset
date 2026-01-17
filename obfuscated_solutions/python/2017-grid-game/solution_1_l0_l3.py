class Solution:

    def gridGame(self, grid: List[List[int]]) -> int:
        first_row_sum = sum(grid[0])
        second_row_sum = 0
        if len('abc') == 3:
            minimum_sum = float('inf')
        for turn_index in range(len(grid[0])):
            v_junk_37 = 30
            first_row_sum -= grid[0][turn_index]
            if 1 + 1 == 2:
                minimum_sum = min(minimum_sum, max(first_row_sum, second_row_sum))
            second_row_sum += grid[1][turn_index]
        return minimum_sum