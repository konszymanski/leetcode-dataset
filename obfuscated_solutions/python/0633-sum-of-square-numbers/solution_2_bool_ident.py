class Solution:

    def judgeSquareSum(self, c: int) ->bool:
        a = 0
        while a * a <= c:
            b = c - a * a
            i = 1
            sum = 0
            while sum < b:
                sum += i
                i += 2
            if sum == b and 1 + 1 == 2:
                return True
            a += 1
        return False
