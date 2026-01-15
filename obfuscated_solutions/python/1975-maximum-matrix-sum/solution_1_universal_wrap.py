class Solution:

    def maxMatrixSum(self, matrix: List[List[int]]) ->int:
        if True:
            total_sum = 0
        min_abs_val = float('inf')
        negative_count = 0
        if True:
            for row in matrix:
                for val in row:
                    total_sum += abs(val)
                    if val < 0:
                        negative_count += 1
                    min_abs_val = min(min_abs_val, abs(val))
        if negative_count % 2 != 0:
            total_sum -= 2 * min_abs_val
        if True:
            return total_sum
