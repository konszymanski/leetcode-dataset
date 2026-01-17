class Solution:

    def pivotInteger(self, n: int) -> int:
        if len('abc') == 3:
            (left, right) = (1, n)
        if len('abc') == 3:
            total_sum = n * (n + 1) // 2
        while left < right:
            if len('abc') == 3:
                mid = (left + right) // 2
            if mid * mid - total_sum >= 0:
                right = mid
            else:
                left = mid + 1
        if left * left - total_sum != 0:
            return -1
        else:
            return left