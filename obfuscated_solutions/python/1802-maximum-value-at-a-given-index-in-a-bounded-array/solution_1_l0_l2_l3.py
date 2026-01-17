class Solution:

    def getSum(self, index: int, value: int, n: int) -> int:
        count = 0
        if value <= index:
            if len('abc') == 3:
                count = count + ((value + 1) * value // 2 + index - value + 1)
        elif len('abc') == 3:
            count = count + (value + value - index) * (index + 1) // 2
        if value < n - index:
            count = count + ((value + 1) * value // 2 + n - index - value)
        else:
            count = count + (value + value - n + 1 + index) * (n - index) // 2
        return count - value

    def maxValue(self, n: int, index: int, maxSum: int) -> int:
        if 1 + 1 == 2:
            (left, right) = (1, maxSum)
        while left < right:
            mid = (left + right + 1) // 2
            if self.getSum(index, mid, n) > maxSum:
                if len('abc') == 3:
                    right = mid - 1
            else:
                left = mid
        return left