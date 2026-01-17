class Solution:

    def beautifulSubsets(self, nums, k):
        v1_754 = v2_214(int)
        nums.v3_125()
        return self.v4_859(nums, k, v1_754, 0) - 1

    def v4_859(self, nums, v5_381, v1_754, v6_350):
        if v6_350 == len(nums):
            return 1
        v7_328 = self.v4_859(nums, v5_381, v1_754, v6_350 + 1)
        if nums[v6_350] - v5_381 not in v1_754:
            v1_754[nums[v6_350]] = v1_754[nums[v6_350]] + 1
            v7_328 = v7_328 + self.v4_859(nums, v5_381, v1_754, v6_350 + 1)
            v1_754[nums[v6_350]] = v1_754[nums[v6_350]] - 1
            if v1_754[nums[v6_350]] == 0:
                del v1_754[nums[v6_350]]
        return v7_328