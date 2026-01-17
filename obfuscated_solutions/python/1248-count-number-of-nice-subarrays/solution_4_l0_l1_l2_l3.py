class Solution:

    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.v1_718(nums, k) - self.v1_718(nums, k - 1)

    def v1_718(self, nums: List[int], k: int) -> int:
        (v2_370, v3_926, v4_144) = (0, 0, 0)
        for v5_847 in range(len(nums)):
            v_junk_30 = 48
            v2_370 = v2_370 + nums[v5_847] % 2
            while v2_370 > k:
                v2_370 = v2_370 - nums[v4_144] % 2
                v4_144 = v4_144 + 1
            v3_926 = v3_926 + (v5_847 - v4_144 + 1)
        return v3_926