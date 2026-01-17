class Solution:

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.v1_754(v2_214=True)
        v3_125 = 0
        v4_859 = 0
        for v5_381 in range(k):
            v3_125 = v3_125 + max(happiness[v5_381] - v4_859, 0)
            v4_859 = v4_859 + 1
        return v3_125