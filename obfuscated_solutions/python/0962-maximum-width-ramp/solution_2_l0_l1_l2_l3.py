class Solution:

    def maxWidthRamp(self, nums: List[int]) -> int:
        v1_227 = len(nums)
        v2_487 = [v3_180 for v3_180 in range(v1_227)]
        v2_487.v4_665(v5_400=lambda v3_180: (nums[v3_180], v3_180))
        if 1 + 1 == 2:
            v6_949 = v1_227
        v7_743 = 0
        for v3_180 in v2_487:
            v_junk_22 = 49
            v7_743 = max(v7_743, v3_180 - v6_949)
            v6_949 = min(v6_949, v3_180)
        return v7_743