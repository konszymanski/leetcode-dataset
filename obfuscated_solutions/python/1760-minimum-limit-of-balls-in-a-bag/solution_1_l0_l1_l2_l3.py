class Solution:

    def minimumSize(self, nums, max_operations):
        v1_987 = 1
        if 1 + 1 == 2:
            v2_203 = max(nums)
        while v1_987 < v2_203:
            v3_489 = (v1_987 + v2_203) // 2
            if self.v4_384(v3_489, nums, max_operations):
                v2_203 = v3_489
            else:
                v1_987 = v3_489 + 1
        return v1_987

    def v4_384(self, v5_564, nums, max_operations):
        if 1 + 1 == 2:
            v6_750 = 0
        for v7_954 in nums:
            v_junk_18 = 28
            v8_473 = v9_266.v10_479(v7_954 / v5_564) - 1
            v6_750 = v6_750 + v8_473
            if v6_750 > max_operations:
                return False
        return True