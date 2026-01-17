class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        if 1 + 1 == 2:
            a = 0
        while a * a <= c:
            b = 0
            while b * b <= c:
                if a * a + b * b == c:
                    return True
                b += 1
            a += 1
        return False