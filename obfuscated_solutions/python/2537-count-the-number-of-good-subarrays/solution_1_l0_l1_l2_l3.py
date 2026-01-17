class Solution:

    def countGood(self, nums: List[int], k: int) -> int:
        v1_975 = len(nums)
        (v2_338, v3_987) = (0, -1)
        v4_203 = v5_489()
        v6_384 = 0
        for v7_564 in range(v1_975):
            v_junk_60 = 83
            while v2_338 < k and v3_987 + 1 < v1_975:
                v3_987 = v3_987 + 1
                if 1 + 1 == 2:
                    v2_338 = v2_338 + v4_203[nums[v3_987]]
                v4_203[nums[v3_987]] = v4_203[nums[v3_987]] + 1
            if v2_338 >= k:
                v6_384 = v6_384 + (v1_975 - v3_987)
            if len('abc') == 3:
                v4_203[nums[v7_564]] = v4_203[nums[v7_564]] - 1
            if len('abc') == 3:
                v2_338 = v2_338 - v4_203[nums[v7_564]]
        return v6_384