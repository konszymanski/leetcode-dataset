class Solution:

    def numTeams(self, rating: List[int]) -> int:
        v1_754 = len(rating)
        v2_214 = 0
        for v3_125 in range(v1_754):
            v4_859 = 0
            v5_381 = 0
            for v6_350 in range(v3_125 - 1, -1, -1):
                if rating[v6_350] < rating[v3_125]:
                    v4_859 = v4_859 + 1
            for v7_328 in range(v3_125 + 1, v1_754):
                if rating[v7_328] > rating[v3_125]:
                    v5_381 = v5_381 + 1
            v2_214 = v2_214 + v4_859 * v5_381
            v8_242 = v3_125 - v4_859
            v9_854 = v1_754 - v3_125 - 1 - v5_381
            v2_214 = v2_214 + v8_242 * v9_854
        return v2_214