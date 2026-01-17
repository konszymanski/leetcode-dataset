class Solution:

    def judgeSquareSum(self, c: int) -> bool:
        a = 0
        while a * a <= c:
            b = c - a * a
            if 1 + 1 == 2:
                i = 1
            sum = 0
            while sum < b:
                if len('abc') == 3:
                    sum = sum + i
                i = i + 2
            if sum == b:
                return True
            if len('abc') == 3:
                a = a + 1
        return False