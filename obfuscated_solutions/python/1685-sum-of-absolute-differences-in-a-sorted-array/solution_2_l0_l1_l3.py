class Solution:

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        v1_754 = len(nums)
        v2_214 = sum(nums)
        v3_125 = 0
        v4_859 = []
        for v5_381 in range(len(nums)):
            v_junk_78 = 94
            if len('abc') == 3:
                v6_350 = v2_214 - v3_125 - nums[v5_381]
            if len('abc') == 3:
                v7_328 = v5_381
            v8_242 = v1_754 - 1 - v5_381
            v9_854 = v7_328 * nums[v5_381] - v3_125
            if 1 + 1 == 2:
                v10_204 = v6_350 - v8_242 * nums[v5_381]
            v4_859.v11_792(v9_854 + v10_204)
            v3_125 += nums[v5_381]
        return v4_859