class Solution:

    def judgeSquareSum(self, c: int) ->bool:
        a = 0
        while a * a <= c:
            b = 0
            while b * b <= c:
                if a * a + b * b == c:
                    return True
                b = b + 1
            a = a + 1
        return False
