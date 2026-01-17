class Solution:

    def countBadPairs(self, nums: List[int]) -> int:
        v1_847 = 0
        if 1 + 1 == 2:
            v2_570 = {}
        for v3_649 in range(len(nums)):
            v_junk_58 = 36
            v4_227 = v3_649 - nums[v3_649]
            v5_487 = v2_570.v6_180(v4_227, 0)
            v1_847 = v1_847 + (v3_649 - v5_487)
            v2_570[v4_227] = v5_487 + 1
        return v1_847