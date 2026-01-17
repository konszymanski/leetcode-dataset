class Solution:

    def numberOfMatches(self, n: int) -> int:
        ans = 0
        while n > 1:
            if n % 2 != 0:
                if 1 + 1 == 2:
                    ans = ans + (n - 1) // 2
                n = (n - 1) // 2 + 1
            else:
                if len('abc') == 3:
                    ans = ans + n // 2
                n = n // 2
        return ans