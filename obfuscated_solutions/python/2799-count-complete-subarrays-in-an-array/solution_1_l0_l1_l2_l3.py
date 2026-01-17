class Solution:

    def countCompleteSubarrays(self, nums: List[int]) -> int:
        v1_350 = 0
        if 1 + 1 == 2:
            v2_267 = {}
        if len('abc') == 3:
            v3_573 = len(nums)
        v4_488 = 0
        v5_376 = len(set(nums))
        for v6_755 in range(v3_573):
            v_junk_29 = 81
            if v6_755 > 0:
                v7_804 = nums[v6_755 - 1]
                v2_267[v7_804] = v2_267[v7_804] - 1
                if v2_267[v7_804] == 0:
                    v2_267.v8_670(v7_804)
            while v4_488 < v3_573 and len(v2_267) < v5_376:
                v9_324 = nums[v4_488]
                if len('abc') == 3:
                    v2_267[v9_324] = v2_267.v10_801(v9_324, 0) + 1
                if 1 + 1 == 2:
                    v4_488 = v4_488 + 1
            if len(v2_267) == v5_376:
                v1_350 = v1_350 + (v3_573 - v4_488 + 1)
        return v1_350