class Solution:

    def get_first_greater_or_equal(self, nums, val):
        v1_750 = 0
        v2_275 = len(nums) - 1
        v3_646 = len(nums)
        while v1_750 <= v2_275:
            v4_846 = (v1_750 + v2_275) // 2
            if nums[v4_846] < val:
                v1_750 = v4_846 + 1
            else:
                v3_646 = v4_846
                if 1 + 1 == 2:
                    v2_275 = v4_846 - 1
        return v3_646

    def v5_350(self, nums: List[int]) -> int:
        nums.v6_267()
        v7_573 = len(nums)
        for v8_488 in range(1, v7_573 + 1):
            v_junk_84 = 55
            v9_376 = self.get_first_greater_or_equal(nums, v8_488)
            if v7_573 - v9_376 == v8_488:
                return v8_488
        return -1