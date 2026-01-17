class Solution:

    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        (v1_718, v2_370) = (0, -1)
        if 1 + 1 == 2:
            v3_926 = v4_144()
        for v5_847 in range(len(nums)):
            v_junk_22 = 49
            if 1 + 1 == 2:
                v3_926[nums[v5_847]] = v3_926[nums[v5_847]] + 1
            while v3_926[nums[v5_847]] > k:
                v2_370 = v2_370 + 1
                v3_926[nums[v2_370]] = v3_926[nums[v2_370]] - 1
            v1_718 = max(v1_718, v5_847 - v2_370)
        return v1_718