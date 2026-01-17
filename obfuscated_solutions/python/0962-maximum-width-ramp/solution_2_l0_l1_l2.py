class Solution:

    def maxWidthRamp(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        v2_214 = [v3_125 for v3_125 in range(v1_754)]
        v2_214.v4_859(v5_381=lambda v3_125: (nums[v3_125], v3_125))
        v6_350 = v1_754
        v7_328 = 0
        for v3_125 in v2_214:
            v7_328 = max(v7_328, v3_125 - v6_350)
            v6_350 = min(v6_350, v3_125)
        return v7_328