class Solution:

    def minIncrementForUnique(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        v2_214 = max(nums)
        v3_125 = 0
        v4_859 = [0] * (v1_754 + v2_214)
        for v5_381 in nums:
            v4_859[v5_381] = v4_859[v5_381] + 1
        for v6_350 in range(len(v4_859)):
            if v4_859[v6_350] <= 1:
                continue
            v7_328 = v4_859[v6_350] - 1
            v4_859[v6_350 + 1] = v4_859[v6_350 + 1] + v7_328
            v4_859[v6_350] = 1
            v3_125 = v3_125 + v7_328
        return v3_125