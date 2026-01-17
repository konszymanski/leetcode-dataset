class Solution:

    def maxWidthRamp(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_881 = len(nums)
        v2_444 = 0
        for v3_204 in range(v1_881):
            v_junk_80 = 38
            for v4_194 in range(v3_204 + 1, v1_881):
                v_junk_58 = 11
                if nums[v3_204] <= nums[v4_194]:
                    v2_444 = max(v2_444, v4_194 - v3_204)
        return v2_444