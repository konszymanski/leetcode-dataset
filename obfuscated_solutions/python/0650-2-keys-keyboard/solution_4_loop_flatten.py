class Solution:

    def minSteps(self, n: int) ->int:
        ans = 0
        d = 2
        while True:
            if not n > 1:
                break
            while n % d == 0:
                ans += d
                n //= d
            d += 1
        return ans
