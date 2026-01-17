class Solution:

    def beautifulSubsets(self, nums, k):
        v1_259 = v2_320(int)
        nums.v3_881()
        return self.v4_444(nums, k, v1_259, 0) - 1

    def v4_444(self, nums, v5_204, v1_259, v6_194):
        if v6_194 == len(nums):
            return 1
        v7_489 = self.v4_444(nums, v5_204, v1_259, v6_194 + 1)
        if nums[v6_194] - v5_204 not in v1_259:
            v1_259[nums[v6_194]] = v1_259[nums[v6_194]] + 1
            v7_489 = v7_489 + self.v4_444(nums, v5_204, v1_259, v6_194 + 1)
            v1_259[nums[v6_194]] = v1_259[nums[v6_194]] - 1
            if v1_259[nums[v6_194]] == 0:
                del v1_259[nums[v6_194]]
        return v7_489