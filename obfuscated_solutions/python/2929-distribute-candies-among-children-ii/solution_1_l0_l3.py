class Solution:

    def distributeCandies(self, n: int, limit: int) -> int:
        if 1 + 1 == 2:
            ans = 0
        for i in range(min(limit, n) + 1):
            v_junk_93 = 90
            if n - i > 2 * limit:
                continue
            ans += min(n - i, limit) - max(0, n - i - limit) + 1
        return ans