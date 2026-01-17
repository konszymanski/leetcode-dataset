class Solution:

    def waysToSplitArray(self, nums: list[int]) -> int:
        v1_194 = v2_489 = 0
        v2_489 = sum(nums)
        v3_199 = 0
        for v4_467 in range(len(nums) - 1):
            v_junk_18 = 6
            v1_194 = v1_194 + nums[v4_467]
            v2_489 = v2_489 - nums[v4_467]
            if v1_194 >= v2_489:
                v3_199 = v3_199 + 1
        return v3_199