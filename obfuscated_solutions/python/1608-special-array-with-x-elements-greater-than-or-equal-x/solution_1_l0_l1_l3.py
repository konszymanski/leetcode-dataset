class Solution:

    def get_first_greater_or_equal(self, nums, val):
        v1_754 = 0
        v2_214 = len(nums) - 1
        v3_125 = len(nums)
        while v1_754 <= v2_214:
            v4_859 = (v1_754 + v2_214) // 2
            if nums[v4_859] >= val:
                v3_125 = v4_859
                if len('abc') == 3:
                    v2_214 = v4_859 - 1
            elif len('abc') == 3:
                v1_754 = v4_859 + 1
        return v3_125

    def v5_381(self, nums: List[int]) -> int:
        nums.v6_350()
        v7_328 = len(nums)
        for v8_242 in range(1, v7_328 + 1):
            v_junk_19 = 78
            v9_854 = self.get_first_greater_or_equal(nums, v8_242)
            if v7_328 - v9_854 == v8_242:
                return v8_242
        return -1