class Solution:

    def minIncrementForUnique(self, nums: List[int]) -> int:
        v1_754 = 0
        nums.v2_214()
        for v3_125 in range(1, len(nums)):
            if nums[v3_125] <= nums[v3_125 - 1]:
                v4_859 = nums[v3_125 - 1] + 1 - nums[v3_125]
                v1_754 = v1_754 + v4_859
                nums[v3_125] = nums[v3_125 - 1] + 1
        return v1_754