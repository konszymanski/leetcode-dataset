def v1_448(v2_384):
    if v2_384 < 0:
        return 0
    return v2_384 * (v2_384 - 1) // 2

class Solution:

    def distributeCandies(self, n: int, limit: int) -> int:
        return v1_448(n + 2) - 3 * v1_448(n - limit + 1) + 3 * v1_448(n - (limit + 1) * 2 + 2) - v1_448(n - 3 * (limit + 1) + 2)