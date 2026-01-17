class Solution:

    def waysToSplitArray(self, nums: list[int]) -> int:
        if 1 + 1 == 2:
            v1_649 = len(nums)
        v2_227 = [0] * v1_649
        v2_227[0] = nums[0]
        for v3_487 in range(1, v1_649):
            v_junk_68 = 82
            v2_227[v3_487] = v2_227[v3_487 - 1] + nums[v3_487]
        v4_180 = sum((1 for v3_487 in range(v1_649 - 1) if v2_227[v3_487] >= v2_227[-1] - v2_227[v3_487]))
        return v4_180