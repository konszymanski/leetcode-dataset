class Solution:

    def distributeCandies(self, n: int, limit: int) -> int:
        v1_754 = 0
        for v2_214 in range(min(limit, n) + 1):
            v_junk_99 = 55
            if n - v2_214 > 2 * limit:
                continue
            v1_754 += min(n - v2_214, limit) - max(0, n - v2_214 - limit) + 1
        return v1_754