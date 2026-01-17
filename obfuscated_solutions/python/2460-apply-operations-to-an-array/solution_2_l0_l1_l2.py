class Solution:

    def applyOperations(self, nums):
        v1_754 = len(nums)
        for v2_214 in range(v1_754 - 1):
            if nums[v2_214] == nums[v2_214 + 1] and nums[v2_214] != 0:
                nums[v2_214] = nums[v2_214] * 2
                nums[v2_214 + 1] = 0
        v3_125 = 0
        for v4_859 in range(v1_754):
            if nums[v4_859] != 0:
                nums[v3_125] = nums[v4_859]
                v3_125 = v3_125 + 1
        while v3_125 < v1_754:
            nums[v3_125] = 0
            v3_125 = v3_125 + 1
        return nums