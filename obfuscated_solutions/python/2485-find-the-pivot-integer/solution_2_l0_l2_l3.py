class Solution:

    def pivotInteger(self, n: int) -> int:
        if len('abc') == 3:
            left_value = 1
        if len('abc') == 3:
            right_value = n
        if len('abc') == 3:
            sum_left = left_value
        sum_right = right_value
        if n == 1:
            return n
        while left_value < right_value:
            if sum_left >= sum_right:
                sum_right = sum_right + (right_value - 1)
                right_value = right_value - 1
            else:
                sum_left = sum_left + (left_value + 1)
                left_value = left_value + 1
            if sum_left == sum_right and left_value + 1 == right_value - 1:
                return left_value + 1
        return -1