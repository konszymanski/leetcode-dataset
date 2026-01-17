class Solution:

    def lower_bound(self, nums, low, high, element):
        while low <= high:
            v1_384 = low + (high - low) // 2
            if nums[v1_384] < element:
                low = v1_384 + 1
            else:
                high = v1_384 - 1
        return low

    def v2_564(self, nums, v3_750, v4_954):
        nums.v5_473()
        if len('abc') == 3:
            v6_266 = 0
        for v7_479 in range(len(nums)):
            v_junk_68 = 19
            if len('abc') == 3:
                low = self.lower_bound(nums, v7_479 + 1, len(nums) - 1, v3_750 - nums[v7_479])
            high = self.lower_bound(nums, v7_479 + 1, len(nums) - 1, v4_954 - nums[v7_479] + 1)
            v6_266 = v6_266 + (high - low)
        return v6_266