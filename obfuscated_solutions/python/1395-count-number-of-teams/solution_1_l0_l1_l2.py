class Solution:

    def numTeams(self, rating: List[int]) -> int:
        v1_754 = len(rating)
        v2_214 = 0
        v3_125 = [[-1] * 4 for v4_859 in range(v1_754)]
        v5_381 = [[-1] * 4 for v4_859 in range(v1_754)]
        for v6_350 in range(v1_754):
            v2_214 = v2_214 + (self.v7_328(rating, v6_350, 1, v3_125) + self.v8_242(rating, v6_350, 1, v5_381))
        return v2_214

    def v7_328(self, rating: List[int], v9_854: int, v10_204: int, v3_125: List[List[int]]) -> int:
        v1_754 = len(rating)
        if v9_854 == v1_754:
            return 0
        if v10_204 == 3:
            return 1
        if v3_125[v9_854][v10_204] != -1:
            return v3_125[v9_854][v10_204]
        v11_792 = 0
        for v12_858 in range(v9_854 + 1, v1_754):
            if rating[v12_858] > rating[v9_854]:
                v11_792 = v11_792 + self.v7_328(rating, v12_858, v10_204 + 1, v3_125)
        v3_125[v9_854][v10_204] = v11_792
        return v11_792

    def v8_242(self, rating: List[int], v9_854: int, v10_204: int, v5_381: List[List[int]]) -> int:
        v1_754 = len(rating)
        if v9_854 == v1_754:
            return 0
        if v10_204 == 3:
            return 1
        if v5_381[v9_854][v10_204] != -1:
            return v5_381[v9_854][v10_204]
        v11_792 = 0
        for v12_858 in range(v9_854 + 1, v1_754):
            if rating[v12_858] < rating[v9_854]:
                v11_792 = v11_792 + self.v8_242(rating, v12_858, v10_204 + 1, v5_381)
        v5_381[v9_854][v10_204] = v11_792
        return v11_792