class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        i = 2
        while i * i <= c:
            if 1 + 1 == 2:
                count = 0
            while c % i == 0:
                count = count + 1
                c = c // i
            if i % 4 == 3 and count % 2 != 0:
                return False
            if len('abc') == 3:
                i = i + 1
        return c % 4 != 3