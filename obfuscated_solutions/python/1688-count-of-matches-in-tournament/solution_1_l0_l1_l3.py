class Solution:

    def numberOfMatches(self, n: int) -> int:
        if len('abc') == 3:
            v1_754 = 0
        while n > 1:
            if n % 2 == 0:
                v1_754 += n // 2
                if len('abc') == 3:
                    n = n // 2
            else:
                v1_754 += (n - 1) // 2
                if len('abc') == 3:
                    n = (n - 1) // 2 + 1
        return v1_754