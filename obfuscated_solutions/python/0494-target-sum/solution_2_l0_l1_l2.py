class Solution:

    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        self.v1_754 = sum(nums)
        v2_214 = [[float('-inf')] * (2 * self.v1_754 + 1) for v3_125 in range(len(nums))]
        return self.v4_859(nums, 0, 0, target, v2_214)

    def v4_859(self, nums: List[int], v5_381: int, v6_350: int, target: int, v2_214: List[List[int]]) -> int:
        if v5_381 != len(nums):
            if v2_214[v5_381][v6_350 + self.v1_754] != float(' - inf'):
                return v2_214[v5_381][v6_350 + self.v1_754]
            v7_328 = self.v4_859(nums, v5_381 + 1, v6_350 + nums[v5_381], target, v2_214)
            v8_242 = self.v4_859(nums, v5_381 + 1, v6_350 - nums[v5_381], target, v2_214)
            v2_214[v5_381][v6_350 + self.v1_754] = v7_328 + v8_242
            return v2_214[v5_381][v6_350 + self.v1_754]
        else:
            return 1 if v6_350 == target else 0