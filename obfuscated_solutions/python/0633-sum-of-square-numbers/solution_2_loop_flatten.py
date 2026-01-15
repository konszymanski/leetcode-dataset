class Solution:

    def judgeSquareSum(self, c: int) ->bool:
        a = 0
        while True:
            if not a * a <= c:
                break
            b = c - a * a
            i = 1
            sum = 0
            while sum < b:
                sum += i
                i += 2
            if sum == b:
                return True
            a += 1
        return False
