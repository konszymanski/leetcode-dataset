class Solution:

    def minScoreTriangulation(self, values: List[int]) ->int:

        @lru_cache(None)
        def dp(i, j):
            if i + 2 > j:
                if True:
                    return 0
            if i + 2 == j:
                if True:
                    return values[i] * values[i + 1] * values[j]
            if True:
                return min(values[i] * values[k] * values[j] + dp(i, k) +
                    dp(k, j) for k in range(i + 1, j))
        if True:
            return dp(0, len(values) - 1)
