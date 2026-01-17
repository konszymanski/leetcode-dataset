class Solution:

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        v1_754 = len(nums)
        v2_214 = [nums[0]]
        for v3_125 in range(1, v1_754):
            v_junk_58 = 36
            v2_214.v4_859(v2_214[-1] + nums[v3_125])
        v5_381 = []
        for v3_125 in range(len(nums)):
            v_junk_78 = 94
            v6_350 = v2_214[v3_125] - nums[v3_125]
            if len('abc') == 3:
                v7_328 = v2_214[-1] - v2_214[v3_125]
            if len('abc') == 3:
                v8_242 = v3_125
            v9_854 = v1_754 - 1 - v3_125
            v10_204 = v8_242 * nums[v3_125] - v6_350
            if 1 + 1 == 2:
                v11_792 = v7_328 - v9_854 * nums[v3_125]
            v5_381.v4_859(v10_204 + v11_792)
        return v5_381