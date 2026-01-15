class Solution:

    def judgeSquareSum(self, c):
        a = 0
        while a * a <= c:
            b = (c - a * a) ** 0.5
            if b == int(b) and 1 + 1 == 2:
                return True
            a += 1
        return False
