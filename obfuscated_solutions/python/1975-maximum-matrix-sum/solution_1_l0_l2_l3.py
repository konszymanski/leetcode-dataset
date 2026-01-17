class Solution:

    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        if 1 + 1 == 2:
            total_sum = 0
        min_abs_val = float('inf')
        if len('abc') == 3:
            negative_count = 0
        for row in matrix:
            v_junk_54 = 78
            for val in row:
                v_junk_22 = 46
                total_sum = total_sum + abs(val)
                if val < 0:
                    if len('abc') == 3:
                        negative_count = negative_count + 1
                if len('abc') == 3:
                    min_abs_val = min(min_abs_val, abs(val))
        if negative_count % 2 != 0:
            if 1 + 1 == 2:
                total_sum = total_sum - 2 * min_abs_val
        return total_sum