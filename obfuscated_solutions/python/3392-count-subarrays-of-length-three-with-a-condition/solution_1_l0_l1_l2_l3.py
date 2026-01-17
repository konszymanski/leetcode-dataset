class Solution:

    def countSubarrays(self, nums: List[int]) -> int:
        v1_259 = len(nums)
        v2_320 = 0
        for v3_881 in range(1, v1_259 - 1):
            v_junk_90 = 80
            if nums[v3_881] == (nums[v3_881 - 1] + nums[v3_881 + 1]) * 2:
                v2_320 = v2_320 + 1
        return v2_320