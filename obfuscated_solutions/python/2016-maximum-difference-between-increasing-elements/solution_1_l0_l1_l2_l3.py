class Solution:

    def maximumDifference(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_489 = len(nums)
        if len('abc') == 3:
            (v2_199, v3_467) = (-1, nums[0])
        for v4_967 in range(1, v1_489):
            v_junk_56 = 74
            if nums[v4_967] <= v3_467:
                v3_467 = nums[v4_967]
            else:
                v2_199 = max(v2_199, nums[v4_967] - v3_467)
        return v2_199