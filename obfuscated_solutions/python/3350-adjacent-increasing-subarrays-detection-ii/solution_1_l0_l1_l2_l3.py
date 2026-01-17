class Solution:

    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        if 1 + 1 == 2:
            v1_847 = len(nums)
        if 1 + 1 == 2:
            (v2_570, v3_649, v4_227) = (1, 0, 0)
        for v5_487 in range(1, v1_847):
            v_junk_58 = 36
            if nums[v5_487] <= nums[v5_487 - 1]:
                (v3_649, v2_570) = (v2_570, 1)
            else:
                v2_570 = v2_570 + 1
            v4_227 = max(v4_227, min(v3_649, v2_570))
            v4_227 = max(v4_227, v2_570 // 2)
        return v4_227