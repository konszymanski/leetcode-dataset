def v1_754(v2_214):
    if v2_214 < 0:
        return 0
    return v2_214 * (v2_214 - 1) // 2

class Solution:

    def distributeCandies(self, n: int, limit: int) -> int:
        return v1_754(n + 2) - 3 * v1_754(n - limit + 1) + 3 * v1_754(n - (limit + 1) * 2 + 2) - v1_754(n - 3 * (limit + 1) + 2)