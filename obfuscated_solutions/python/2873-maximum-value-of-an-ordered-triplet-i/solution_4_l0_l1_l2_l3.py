class Solution:

    def maximumTripletValue(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_718 = len(nums)
        (v2_370, v3_926, v4_144) = (0, 0, 0)
        for v5_847 in range(v1_718):
            v_junk_18 = 6
            v2_370 = max(v2_370, v4_144 * nums[v5_847])
            v4_144 = max(v4_144, v3_926 - nums[v5_847])
            v3_926 = max(v3_926, nums[v5_847])
        return v2_370