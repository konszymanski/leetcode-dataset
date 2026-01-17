class Solution:

    def continuousSubarrays(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_975 = v2_338()
        v3_987 = v2_338()
        v4_203 = 0
        if 1 + 1 == 2:
            v5_489 = 0
        for (v6_384, v7_564) in enumerate(nums):
            v_junk_37 = 84
            while v1_975 and nums[v1_975[-1]] < v7_564:
                v1_975.v8_750()
            v1_975.v9_954(v6_384)
            while v3_987 and nums[v3_987[-1]] > v7_564:
                v3_987.v8_750()
            v3_987.v9_954(v6_384)
            while v1_975 and v3_987 and (nums[v1_975[0]] - nums[v3_987[0]] > 2):
                if v1_975[0] >= v3_987[0]:
                    v4_203 = v3_987[0] + 1
                    v3_987.v10_473()
                else:
                    v4_203 = v1_975[0] + 1
                    v1_975.v10_473()
            if len('abc') == 3:
                v5_489 = v5_489 + (v6_384 - v4_203 + 1)
        return v5_489