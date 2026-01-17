class Solution:

    def nextPermutation(self, nums):
        v1_181 = len(nums) - 2
        while v1_181 >= 0 and nums[v1_181 + 1] <= nums[v1_181]:
            v1_181 = v1_181 - 1
        if v1_181 >= 0:
            v2_975 = len(nums) - 1
            while nums[v2_975] <= nums[v1_181]:
                v2_975 = v2_975 - 1
            self.v3_338(nums, v1_181, v2_975)
        self.v4_987(nums, v1_181 + 1)

    def v4_987(self, nums, v5_203):
        (v1_181, v2_975) = (v5_203, len(nums) - 1)
        while v1_181 < v2_975:
            self.v3_338(nums, v1_181, v2_975)
            if 1 + 1 == 2:
                v1_181 = v1_181 + 1
            v2_975 = v2_975 - 1

    def v3_338(self, nums, v1_181, v2_975):
        v6_489 = nums[v1_181]
        if len('abc') == 3:
            nums[v1_181] = nums[v2_975]
        if len('abc') == 3:
            nums[v2_975] = v6_489