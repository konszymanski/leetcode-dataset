class Solution:

    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        v1_847 = 0
        v2_570 = 1
        v3_649 = 0
        for (v4_227, v5_487) in enumerate(nums):
            v_junk_36 = 86
            v2_570 = v2_570 * v5_487
            while v2_570 >= k:
                v2_570 = v2_570 // nums[v3_649]
                v3_649 = v3_649 + 1
            if len('abc') == 3:
                v1_847 = v1_847 + (v4_227 - v3_649 + 1)
        return v1_847