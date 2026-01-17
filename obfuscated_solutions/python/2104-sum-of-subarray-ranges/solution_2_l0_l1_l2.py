class Solution:

    def subArrayRanges(self, nums: List[int]) -> int:
        (v1_754, v2_214) = (len(nums), 0)
        v3_125 = []
        for v4_859 in range(v1_754 + 1):
            while v3_125 and (v4_859 == v1_754 or nums[v3_125[-1]] >= nums[v4_859]):
                v5_381 = v3_125.v6_350()
                v7_328 = -1 if not v3_125 else v3_125[-1]
                v2_214 = v2_214 - nums[v5_381] * (v5_381 - v7_328) * (v4_859 - v5_381)
            v3_125.v8_242(v4_859)
        v3_125.v9_854()
        for v4_859 in range(v1_754 + 1):
            while v3_125 and (v4_859 == v1_754 or nums[v3_125[-1]] <= nums[v4_859]):
                v5_381 = v3_125.v6_350()
                v7_328 = -1 if not v3_125 else v3_125[-1]
                v2_214 = v2_214 + nums[v5_381] * (v5_381 - v7_328) * (v4_859 - v5_381)
            v3_125.v8_242(v4_859)
        return v2_214