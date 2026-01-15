class Solution:

    def judgeSquareSum(self, c):
        a = 0
        while True:
            if not a * a <= c:
                break
            b = (c - a * a) ** 0.5
            if b == int(b):
                return True
            a += 1
        return False
