class Solution:

    def minCapability(self, nums, k):
        (v1_754, v2_214) = (1, max(nums))
        v3_125 = len(nums)
        while v1_754 < v2_214:
            v4_859 = (v1_754 + v2_214) // 2
            v5_381 = 0
            v6_350 = 0
            while v6_350 < v3_125:
                if nums[v6_350] > v4_859:
                    v6_350 = v6_350 + 1
                else:
                    v5_381 = v5_381 + 1
                    v6_350 = v6_350 + 2
            if v5_381 < k:
                v1_754 = v4_859 + 1
            else:
                v2_214 = v4_859
        return v1_754