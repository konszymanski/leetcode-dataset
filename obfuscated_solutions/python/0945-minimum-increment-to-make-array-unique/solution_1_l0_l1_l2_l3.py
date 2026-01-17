class Solution:

    def minIncrementForUnique(self, nums: List[int]) -> int:
        v1_194 = 0
        nums.v2_489()
        for v3_199 in range(1, len(nums)):
            v_junk_15 = 85
            if nums[v3_199] <= nums[v3_199 - 1]:
                v4_467 = nums[v3_199 - 1] + 1 - nums[v3_199]
                v1_194 = v1_194 + v4_467
                nums[v3_199] = nums[v3_199 - 1] + 1
        return v1_194