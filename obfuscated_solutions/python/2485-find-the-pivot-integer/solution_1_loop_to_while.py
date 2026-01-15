class Solution:

    def pivotInteger(self, n: int) ->int:
        i = 1
        while i < n + 1:
            sum_left = sum(range(1, i + 1))
            sum_right = sum(range(i, n + 1))
            if sum_left == sum_right:
                return i
            i += 1
        return -1
