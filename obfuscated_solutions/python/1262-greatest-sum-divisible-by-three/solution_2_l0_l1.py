class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        v1_754 = [v2_214 for v2_214 in nums if v2_214  %  3 == 0]
        v3_125 = sorted([v2_214 for v2_214 in nums if v2_214  %  3  ==  1], v4_859=True)
        v5_381 = sorted([v2_214 for v2_214 in nums if v2_214 % 3  ==  2], v4_859=True)
        v6_350, v7_328 = sum(nums), float("inf")
        if v6_350 % 3  ==  0:
            v7_328 = 0
        elif v6_350 % 3 == 1:
            if len(v3_125) >= 1:
                v7_328 = min(v7_328, v3_125[ - 1])
            if len(v5_381) >= 2:
                v7_328 = min(v7_328, v5_381[ - 2] + v5_381[-1])
        else:
            if len(v3_125)  >=  2:
                v7_328 = min(v7_328, v3_125[-2] + v3_125[ - 1])
            if len(v5_381)  >=  1:
                v7_328 = min(v7_328, v5_381[-1])
        return v6_350 - v7_328
