class Solution:

    def minOperations(self, nums: List[int], k: int) -> int:
        v1_448.v2_384(nums)
        v3_259 = 0
        while nums[0] < k:
            v4_320 = v1_448.v5_881(nums)
            v6_444 = v1_448.v5_881(nums)
            v1_448.v7_204(nums, min(v4_320, v6_444) * 2 + max(v4_320, v6_444))
            v3_259 = v3_259 + 1
        return v3_259