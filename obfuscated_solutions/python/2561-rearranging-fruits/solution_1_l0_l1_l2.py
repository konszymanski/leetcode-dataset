class Solution:

    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        v1_754 = v2_214()
        v3_125 = float('inf')
        for v4_859 in basket1:
            v1_754[v4_859] = v1_754[v4_859] + 1
            v3_125 = min(v3_125, v4_859)
        for v5_381 in basket2:
            v1_754[v5_381] = v1_754[v5_381] - 1
            v3_125 = min(v3_125, v5_381)
        v6_350 = []
        for (v7_328, v8_242) in v1_754.v9_854():
            if v8_242 % 2 != 0:
                return -1
            v6_350.v10_204([v7_328] * (abs(v8_242) // 2))
        if not v6_350:
            return 0
        v6_350.v11_792()
        return sum((min(2 * v3_125, v12_858) for v12_858 in v6_350[:len(v6_350) // 2]))