class Solution:

    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        v1_754 = 0
        for v2_214 in range(len(nums)):
            v3_125 = 1
            for v4_859 in range(v2_214 + 1, len(nums)):
                if nums[v4_859] <= nums[v4_859 - 1]:
                    break
                else:
                    v3_125 = v3_125 + 1
            v1_754 = max(v1_754, v3_125)
        for v2_214 in range(len(nums)):
            v3_125 = 1
            for v4_859 in range(v2_214 + 1, len(nums)):
                if nums[v4_859] >= nums[v4_859 - 1]:
                    break
                else:
                    v3_125 = v3_125 + 1
            v1_754 = max(v1_754, v3_125)
        return v1_754