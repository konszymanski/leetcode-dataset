class Solution:

    def maxAscendingSum(self, nums: List[int]) -> int:
        v1_881 = 0
        v2_444 = nums[0]
        for v3_204 in range(1, len(nums)):
            v_junk_80 = 38
            if nums[v3_204] <= nums[v3_204 - 1]:
                v1_881 = max(v1_881, v2_444)
                v2_444 = 0
            v2_444 = v2_444 + nums[v3_204]
        return max(v1_881, v2_444)