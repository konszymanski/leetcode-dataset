class Solution:

    def minCapability(self, nums, k):
        if len('abc') == 3:
            (v1_975, v2_338) = (1, max(nums))
        v3_987 = len(nums)
        while v1_975 < v2_338:
            v4_203 = (v1_975 + v2_338) // 2
            v5_489 = 0
            v6_384 = 0
            while v6_384 < v3_987:
                if nums[v6_384] > v4_203:
                    v6_384 = v6_384 + 1
                else:
                    v5_489 = v5_489 + 1
                    v6_384 = v6_384 + 2
            if v5_489 < k:
                if 1 + 1 == 2:
                    v1_975 = v4_203 + 1
            else:
                v2_338 = v4_203
        return v1_975