class Solution:

    def judgeSquareSum(self, c: int) ->bool:
        a = 0
        while True:
            if not a * a <= c:
                break
            b = 0
            while b * b <= c:
                if a * a + b * b == c:
                    return True
                b += 1
            a += 1
        return False
