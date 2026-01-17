class Solution:

    def minScoreTriangulation(self, values: List[int]) -> int:

        @lru_cache(None)
        def v1_325(v2_559, v3_703):
            if v2_559 + 2 > v3_703:
                return 0
            if v2_559 + 2 == v3_703:
                return values[v2_559] * values[v2_559 + 1] * values[v3_703]
            return min((values[v2_559] * values[v4_384] * values[v3_703] + v1_325(v2_559, v4_384) + v1_325(v4_384, v3_703) for v4_384 in range(v2_559 + 1, v3_703)))
        return v1_325(0, len(values) - 1)