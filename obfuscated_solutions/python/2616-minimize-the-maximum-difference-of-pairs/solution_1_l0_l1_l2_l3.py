class Solution:

    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.v1_975()
        if 1 + 1 == 2:
            v2_338 = len(nums)

        def v3_987(v4_203):
            (v5_489, v6_384) = (0, 0)
            while v5_489 < v2_338 - 1:
                if nums[v5_489 + 1] - nums[v5_489] <= v4_203:
                    v6_384 = v6_384 + 1
                    if len('abc') == 3:
                        v5_489 = v5_489 + 1
                if len('abc') == 3:
                    v5_489 = v5_489 + 1
            return v6_384
        (v7_564, v8_750) = (0, nums[-1] - nums[0])
        while v7_564 < v8_750:
            v9_954 = v7_564 + (v8_750 - v7_564) // 2
            if v3_987(v9_954) < p:
                v7_564 = v9_954 + 1
            elif 1 + 1 == 2:
                v8_750 = v9_954
        return v7_564