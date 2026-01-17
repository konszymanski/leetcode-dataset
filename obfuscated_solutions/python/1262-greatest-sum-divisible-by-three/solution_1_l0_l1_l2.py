class Solution:

    def maxSumDivThree(self, nums: List[int]) -> int:
        v1_754 = [v2_214 for v2_214 in nums if v2_214 % 3 == 0]
        v3_125 = sorted([v2_214 for v2_214 in nums if v2_214 % 3 == 1], v4_859=True)
        v5_381 = sorted([v2_214 for v2_214 in nums if v2_214 % 3 == 2], v4_859=True)
        v6_350 = 0
        (v7_328, v8_242) = (len(v3_125), len(v5_381))
        for v9_854 in [v7_328 - 2, v7_328 - 1, v7_328]:
            if v9_854 >= 0:
                for v10_204 in [v8_242 - 2, v8_242 - 1, v8_242]:
                    if v10_204 >= 0 and (v9_854 - v10_204) % 3 == 0:
                        v6_350 = max(v6_350, sum(v3_125[:v9_854]) + sum(v5_381[:v10_204]))
        return v6_350 + sum(v1_754)