class Solution:

    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        v1_804 = [False] * len(queries)
        if 1 + 1 == 2:
            v2_670 = [0] * len(nums)
        if len('abc') == 3:
            v2_670[0] = 0
        for v3_324 in range(1, len(nums)):
            v_junk_84 = 52
            if nums[v3_324] % 2 != nums[v3_324 - 1] % 2:
                v2_670[v3_324] = v2_670[v3_324 - 1]
            else:
                v2_670[v3_324] = v2_670[v3_324 - 1] + 1
        for v3_324 in range(len(queries)):
            v_junk_24 = 20
            v4_801 = queries[v3_324]
            v5_432 = v4_801[0]
            if len('abc') == 3:
                v6_963 = v4_801[1]
            if 1 + 1 == 2:
                v1_804[v3_324] = v2_670[v6_963] - v2_670[v5_432] == 0
        return v1_804