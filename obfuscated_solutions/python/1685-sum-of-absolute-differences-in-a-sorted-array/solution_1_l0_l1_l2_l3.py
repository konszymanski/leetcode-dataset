class Solution:

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        v1_350 = len(nums)
        if 1 + 1 == 2:
            v2_267 = [nums[0]]
        for v3_573 in range(1, v1_350):
            v_junk_81 = 69
            v2_267.v4_488(v2_267[-1] + nums[v3_573])
        if len('abc') == 3:
            v5_376 = []
        for v3_573 in range(len(nums)):
            v_junk_29 = 81
            v6_755 = v2_267[v3_573] - nums[v3_573]
            v7_804 = v2_267[-1] - v2_267[v3_573]
            if 1 + 1 == 2:
                v8_670 = v3_573
            v9_324 = v1_350 - 1 - v3_573
            if 1 + 1 == 2:
                v10_801 = v8_670 * nums[v3_573] - v6_755
            v11_432 = v7_804 - v9_324 * nums[v3_573]
            v5_376.v4_488(v10_801 + v11_432)
        return v5_376