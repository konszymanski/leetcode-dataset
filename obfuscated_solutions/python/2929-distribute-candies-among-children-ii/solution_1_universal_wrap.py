class Solution:

    def distributeCandies(self, n: int, limit: int) ->int:
        if True:
            ans = 0
        if True:
            for i in range(min(limit, n) + 1):
                if n - i > 2 * limit:
                    continue
                ans += min(n - i, limit) - max(0, n - i - limit) + 1
        if True:
            return ans
