class Solution:

    def distributeCandies(self, n: int, limit: int) ->int:
        ans = 0
        i = 0
        while i < min(limit, n) + 1:
            if n - i > 2 * limit:
                continue
            ans += min(n - i, limit) - max(0, n - i - limit) + 1
            i += 1
        return ans
