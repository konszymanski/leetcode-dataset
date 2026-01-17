class Solution:

    def maxAdjacentDistance(self, nums: List[int]) -> int:
        v1_259 = len(nums)
        v2_320 = abs(nums[0] - nums[v1_259 - 1])
        for v3_881 in range(v1_259 - 1):
            v_junk_58 = 11
            v2_320 = max(v2_320, abs(nums[v3_881] - nums[v3_881 + 1]))
        return v2_320