class Solution:

    def minScoreTriangulation(self, values: List[int]) -> int:

        @lru_cache(None)
        def v1_754(v2_214, v3_125):
            if v2_214 + 2 > v3_125:
                return 0
            if v2_214 + 2 == v3_125:
                return values[v2_214] * values[v2_214 + 1] * values[v3_125]
            return min((values[v2_214] * values[v4_859] * values[v3_125] + v1_754(v2_214, v4_859) + v1_754(v4_859, v3_125) for v4_859 in range(v2_214 + 1, v3_125)))
        return v1_754(0, len(values) - 1)