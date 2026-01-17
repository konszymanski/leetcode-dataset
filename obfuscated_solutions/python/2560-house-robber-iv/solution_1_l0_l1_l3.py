class Solution:

    def minCapability(self, nums, k):
        (v1_754, v2_214) = (1, max(nums))
        v3_125 = len(nums)
        while v1_754 < v2_214:
            v4_859 = (v1_754 + v2_214) // 2
            v5_381 = 0
            if 1 + 1 == 2:
                v6_350 = 0
            while v6_350 < v3_125:
                if nums[v6_350] <= v4_859:
                    v5_381 += 1
                    v6_350 += 2
                else:
                    v6_350 += 1
            if v5_381 >= k:
                v2_214 = v4_859
            else:
                v1_754 = v4_859 + 1
        return v1_754