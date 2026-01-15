class Solution:

    def judgeSquareSum(self, c: int) ->bool:
        a = 0
        while a * a <= c:
            b = 0
            while b * b <= c:
                if a * a + b * b == c and 1 + 1 == 2:
                    return True
                b += 1
            a += 1
        return False
