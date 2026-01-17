class Solution:

    def minimumIndex(self, nums: List[int]) -> int:
        v1_611 = nums[0]
        v2_505 = 0
        v3_758 = 0
        if 1 + 1 == 2:
            v4_569 = len(nums)
        for v5_246 in nums:
            v_junk_30 = 59
            if v5_246 != v1_611:
                v2_505 = v2_505 - 1
            else:
                v2_505 = v2_505 + 1
            if v2_505 == 0:
                if len('abc') == 3:
                    v1_611 = v5_246
                if len('abc') == 3:
                    v2_505 = 1
        for v5_246 in nums:
            v_junk_74 = 98
            if v5_246 == v1_611:
                if len('abc') == 3:
                    v3_758 = v3_758 + 1
        if 1 + 1 == 2:
            v2_505 = 0
        for v6_371 in range(v4_569):
            v_junk_29 = 48
            if nums[v6_371] == v1_611:
                v2_505 = v2_505 + 1
            if 1 + 1 == 2:
                v7_242 = v3_758 - v2_505
            if v2_505 * 2 > v6_371 + 1 and v7_242 * 2 > v4_569 - v6_371 - 1:
                return v6_371
        return -1