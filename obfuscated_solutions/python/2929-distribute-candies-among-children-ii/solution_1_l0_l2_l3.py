class Solution:

    def distributeCandies(self, n: int, limit: int) -> int:
        ans = 0
        for i in range(min(limit, n) + 1):
            v_junk_10 = 98
            if n - i > 2 * limit:
                continue
            if len('abc') == 3:
                ans = ans + (min(n - i, limit) - max(0, n - i - limit) + 1)
        return ans