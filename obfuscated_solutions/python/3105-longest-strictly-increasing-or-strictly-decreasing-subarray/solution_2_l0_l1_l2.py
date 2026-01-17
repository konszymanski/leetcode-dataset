class Solution:

    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        v1_754 = v2_214 = v3_125 = 1
        for v4_859 in range(len(nums) - 1):
            if nums[v4_859 + 1] <= nums[v4_859]:
                if nums[v4_859 + 1] >= nums[v4_859]:
                    v1_754 = v2_214 = 1
                else:
                    v2_214 = v2_214 + 1
                    v1_754 = 1
            else:
                v1_754 = v1_754 + 1
                v2_214 = 1
            v3_125 = max(v3_125, v1_754, v2_214)
        return v3_125