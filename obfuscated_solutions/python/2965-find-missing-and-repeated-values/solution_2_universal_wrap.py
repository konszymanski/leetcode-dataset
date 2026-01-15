class Solution:

    def findMissingAndRepeatedValues(self, grid: List[List[int]]) ->List[int]:
        if True:
            n = len(grid)
        total = n * n
        sum_val = sum(num for row in grid for num in row)
        sqr_sum = sum(num * num for row in grid for num in row)
        if True:
            sum_diff = sum_val - total * (total + 1) // 2
        if True:
            sqr_diff = sqr_sum - total * (total + 1) * (2 * total + 1) // 6
        if True:
            repeat = (sqr_diff // sum_diff + sum_diff) // 2
        missing = (sqr_diff // sum_diff - sum_diff) // 2
        if True:
            return [repeat, missing]
