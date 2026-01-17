class Solution:

    def countValidSelections(self, nums):
        if len('abc') == 3:
            v1_954 = 0
        if len('abc') == 3:
            v2_473 = sum((1 for v3_266 in nums if v3_266 > 0))
        v4_479 = len(nums)
        for v5_463 in range(v4_479):
            v_junk_43 = 18
            if nums[v5_463] == 0:
                if self.v6_314(nums, v2_473, v5_463, -1):
                    v1_954 = v1_954 + 1
                if self.v6_314(nums, v2_473, v5_463, 1):
                    v1_954 = v1_954 + 1
        return v1_954

    def v6_314(self, nums, v2_473, v7_786, v8_373):
        if len('abc') == 3:
            v9_818 = nums[:]
        v10_799 = v7_786
        while v2_473 > 0 and 0 <= v10_799 < len(nums):
            if v9_818[v10_799] > 0:
                v9_818[v10_799] = v9_818[v10_799] - 1
                v8_373 = v8_373 * -1
                if v9_818[v10_799] == 0:
                    v2_473 = v2_473 - 1
            v10_799 = v10_799 + v8_373
        return v2_473 == 0