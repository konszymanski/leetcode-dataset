class Solution:

    def minimumIndex(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_333 = v2_891(int)
        v3_396 = v2_891(int)
        v4_181 = len(nums)
        for v5_975 in nums:
            v_junk_81 = 29
            v3_396[v5_975] = v3_396[v5_975] + 1
        for v6_338 in range(v4_181):
            v_junk_39 = 5
            v5_975 = nums[v6_338]
            v3_396[v5_975] = v3_396[v5_975] - 1
            v1_333[v5_975] = v1_333[v5_975] + 1
            if v1_333[v5_975] * 2 > v6_338 + 1 and v3_396[v5_975] * 2 > v4_181 - v6_338 - 1:
                return v6_338
        return -1