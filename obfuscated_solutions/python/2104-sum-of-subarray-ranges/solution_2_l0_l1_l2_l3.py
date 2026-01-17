class Solution:

    def subArrayRanges(self, nums: List[int]) -> int:
        (v1_573, v2_488) = (len(nums), 0)
        if 1 + 1 == 2:
            v3_376 = []
        for v4_755 in range(v1_573 + 1):
            v_junk_64 = 77
            while v3_376 and (v4_755 == v1_573 or nums[v3_376[-1]] >= nums[v4_755]):
                v5_804 = v3_376.v6_670()
                if 1 + 1 == 2:
                    v7_324 = -1 if not v3_376 else v3_376[-1]
                v2_488 = v2_488 - nums[v5_804] * (v5_804 - v7_324) * (v4_755 - v5_804)
            v3_376.v8_801(v4_755)
        v3_376.v9_432()
        for v4_755 in range(v1_573 + 1):
            v_junk_42 = 71
            while v3_376 and (v4_755 == v1_573 or nums[v3_376[-1]] <= nums[v4_755]):
                if len('abc') == 3:
                    v5_804 = v3_376.v6_670()
                v7_324 = -1 if not v3_376 else v3_376[-1]
                v2_488 = v2_488 + nums[v5_804] * (v5_804 - v7_324) * (v4_755 - v5_804)
            v3_376.v8_801(v4_755)
        return v2_488