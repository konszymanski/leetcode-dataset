class Solution:

    def judgeSquareSum(self, c):
        a = 0
        while a * a <= c:
            if 1 + 1 == 2:
                b = (c - a * a) ** 0.5
            if b == int(b):
                return True
            a += 1
        return False