class Solution:

    def countSubarrays(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        v2_214 = 0
        for v3_125 in range(1, v1_754 - 1):
            if nums[v3_125] == (nums[v3_125 - 1] + nums[v3_125 + 1]) * 2:
                v2_214 = v2_214 + 1
        return v2_214