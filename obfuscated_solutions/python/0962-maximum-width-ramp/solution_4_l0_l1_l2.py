class Solution:

    def maxWidthRamp(self, nums):
        v1_754 = len(nums)
        v2_214 = []
        for v3_125 in range(v1_754):
            if not v2_214 or nums[v2_214[-1]] > nums[v3_125]:
                v2_214.v4_859(v3_125)
        v5_381 = 0
        for v6_350 in range(v1_754 - 1, -1, -1):
            while v2_214 and nums[v2_214[-1]] <= nums[v6_350]:
                v5_381 = max(v5_381, v6_350 - v2_214[-1])
                v2_214.v7_328()
        return v5_381