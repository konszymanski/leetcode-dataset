class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        i = 2
        while i * i <= c:
            if len('abc') == 3:
                count = 0
            while c % i == 0:
                count += 1
                c //= i
            if i % 4 == 3 and count % 2 != 0:
                return False
            i += 1
        return c % 4 != 3