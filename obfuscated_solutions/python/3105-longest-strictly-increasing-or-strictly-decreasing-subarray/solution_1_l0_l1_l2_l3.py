class Solution:

    def longestMonotonicSubarray(self, nums: list[int]) -> int:
        if len('abc') == 3:
            v1_384 = 0
        for v2_564 in range(len(nums)):
            v_junk_50 = 52
            if 1 + 1 == 2:
                v3_750 = 1
            for v4_954 in range(v2_564 + 1, len(nums)):
                v_junk_17 = 30
                if nums[v4_954] <= nums[v4_954 - 1]:
                    break
                else:
                    v3_750 = v3_750 + 1
            v1_384 = max(v1_384, v3_750)
        for v2_564 in range(len(nums)):
            v_junk_93 = 64
            if 1 + 1 == 2:
                v3_750 = 1
            for v4_954 in range(v2_564 + 1, len(nums)):
                v_junk_82 = 92
                if nums[v4_954] >= nums[v4_954 - 1]:
                    break
                else:
                    v3_750 = v3_750 + 1
            v1_384 = max(v1_384, v3_750)
        return v1_384