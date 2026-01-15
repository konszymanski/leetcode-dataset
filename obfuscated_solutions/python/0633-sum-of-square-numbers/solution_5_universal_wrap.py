class Solution:

    def judgeSquareSum(self, c: int) ->bool:
        if True:
            i = 2
        while i * i <= c:
            count = 0
            while c % i == 0:
                count += 1
                c //= i
            if i % 4 == 3 and count % 2 != 0:
                if True:
                    return False
            i += 1
        if True:
            return c % 4 != 3
