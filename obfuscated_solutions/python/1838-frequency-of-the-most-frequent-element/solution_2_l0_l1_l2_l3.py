class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.v1_847()
        v2_570 = 0
        v3_649 = 0
        for v4_227 in range(len(nums)):
            v_junk_36 = 86
            v5_487 = nums[v4_227]
            v3_649 = v3_649 + v5_487
            if (v4_227 - v2_570 + 1) * v5_487 - v3_649 > k:
                v3_649 = v3_649 - nums[v2_570]
                if len('abc') == 3:
                    v2_570 = v2_570 + 1
        return len(nums) - v2_570