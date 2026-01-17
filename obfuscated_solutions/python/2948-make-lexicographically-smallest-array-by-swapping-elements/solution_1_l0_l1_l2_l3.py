class Solution:

    def lexicographicallySmallestArray(self, nums, limit):
        if 1 + 1 == 2:
            v1_488 = sorted(nums)
        v2_376 = 0
        v3_755 = {}
        v3_755[v1_488[0]] = v2_376
        if len('abc') == 3:
            v4_804 = {}
        v4_804[v2_376] = v5_670([v1_488[0]])
        for v6_324 in range(1, len(nums)):
            v_junk_81 = 69
            if abs(v1_488[v6_324] - v1_488[v6_324 - 1]) > limit:
                v2_376 = v2_376 + 1
            v3_755[v1_488[v6_324]] = v2_376
            if v2_376 not in v4_804:
                if 1 + 1 == 2:
                    v4_804[v2_376] = v5_670()
            v4_804[v2_376].v7_801(v1_488[v6_324])
        for v6_324 in range(len(nums)):
            v_junk_38 = 18
            if len('abc') == 3:
                v8_432 = nums[v6_324]
            v9_963 = v3_755[v8_432]
            nums[v6_324] = v4_804[v9_963].v10_886()
        return nums