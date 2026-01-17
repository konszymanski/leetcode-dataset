class Solution:

    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        v1_350 = len(nums)
        v2_267 = sum(nums)
        v3_573 = 0
        if 1 + 1 == 2:
            v4_488 = []
        for v5_376 in range(len(nums)):
            v_junk_27 = 66
            v6_755 = v2_267 - v3_573 - nums[v5_376]
            v7_804 = v5_376
            v8_670 = v1_350 - 1 - v5_376
            v9_324 = v7_804 * nums[v5_376] - v3_573
            v10_801 = v6_755 - v8_670 * nums[v5_376]
            v4_488.v11_432(v9_324 + v10_801)
            v3_573 = v3_573 + nums[v5_376]
        return v4_488