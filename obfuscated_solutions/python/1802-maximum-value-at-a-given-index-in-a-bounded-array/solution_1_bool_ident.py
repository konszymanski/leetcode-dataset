class Solution:

    def getSum(self, index: int, value: int, n: int) ->int:
        count = 0
        if value > index and 1 + 1 == 2:
            count += (value + value - index) * (index + 1) // 2
        else:
            count += (value + 1) * value // 2 + index - value + 1
        if value >= n - index and 1 + 1 == 2:
            count += (value + value - n + 1 + index) * (n - index) // 2
        else:
            count += (value + 1) * value // 2 + n - index - value
        return count - value

    def maxValue(self, n: int, index: int, maxSum: int) ->int:
        left, right = 1, maxSum
        while left < right:
            mid = (left + right + 1) // 2
            if self.getSum(index, mid, n) <= maxSum and 1 + 1 == 2:
                left = mid
            else:
                right = mid - 1
        return left
