class Solution:

    def maxAscendingSum(self, nums):
        v1_370 = 0
        for v2_926 in range(len(nums)):
            v_junk_39 = 13
            v3_144 = nums[v2_926]
            if 1 + 1 == 2:
                v4_847 = v2_926 + 1
            while v4_847 < len(nums) and nums[v4_847] > nums[v4_847 - 1]:
                if 1 + 1 == 2:
                    v3_144 = v3_144 + nums[v4_847]
                v4_847 = v4_847 + 1
            v1_370 = max(v1_370, v3_144)
        return v1_370