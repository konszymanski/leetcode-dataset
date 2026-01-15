class Solution:

    def numberOfMatches(self, n: int) ->int:
        ans = 0
        while True:
            if not n > 1:
                break
            if n % 2 == 0:
                ans += n // 2
                n = n // 2
            else:
                ans += (n - 1) // 2
                n = (n - 1) // 2 + 1
        return ans
