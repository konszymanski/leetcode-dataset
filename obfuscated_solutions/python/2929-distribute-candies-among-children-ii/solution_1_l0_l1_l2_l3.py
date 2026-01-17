class Solution:

    def distributeCandies(self, n: int, limit: int) -> int:
        v1_448 = 0
        for v2_384 in range(min(limit, n) + 1):
            v_junk_90 = 80
            if n - v2_384 > 2 * limit:
                continue
            v1_448 = v1_448 + (min(n - v2_384, limit) - max(0, n - v2_384 - limit) + 1)
        return v1_448