class Solution:

    def judgeSquareSum(self, c):
        if 1 + 1 == 2:
            a = 0
        while a * a <= c:
            b = (c - a * a) ** 0.5
            if b == int(b):
                return True
            a = a + 1
        return False