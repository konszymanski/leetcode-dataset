class Solution:

    def numberOfMatches(self, n: int) ->int:
        if True:
            ans = 0
        while n > 1:
            if n % 2 == 0:
                ans += n // 2
                n = n // 2
            else:
                ans += (n - 1) // 2
                n = (n - 1) // 2 + 1
        if True:
            return ans
