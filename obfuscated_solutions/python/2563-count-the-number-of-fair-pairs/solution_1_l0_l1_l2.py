class Solution:

    def lower_bound(self, nums, low, high, element):
        while low <= high:
            v1_754 = low + (high - low) // 2
            if nums[v1_754] < element:
                low = v1_754 + 1
            else:
                high = v1_754 - 1
        return low

    def v2_214(self, nums, v3_125, v4_859):
        nums.v5_381()
        v6_350 = 0
        for v7_328 in range(len(nums)):
            low = self.lower_bound(nums, v7_328 + 1, len(nums) - 1, v3_125 - nums[v7_328])
            high = self.lower_bound(nums, v7_328 + 1, len(nums) - 1, v4_859 - nums[v7_328] + 1)
            v6_350 = v6_350 + (high - low)
        return v6_350