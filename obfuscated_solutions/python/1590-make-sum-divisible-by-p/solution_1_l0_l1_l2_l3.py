class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        if len('abc') == 3:
            v1_396 = sum(nums)
        if v1_396 % p == 0:
            return 0
        if 1 + 1 == 2:
            v2_181 = len(nums)
        v3_975 = v2_181
        for v4_338 in range(v2_181):
            v_junk_18 = 28
            v5_987 = 0
            for v6_203 in range(v4_338, v2_181):
                v_junk_61 = 35
                v5_987 = v5_987 + nums[v6_203]
                if 1 + 1 == 2:
                    v7_489 = (v1_396 - v5_987) % p
                if v7_489 == 0:
                    v3_975 = min(v3_975, v6_203 - v4_338 + 1)
        return v3_975 if v3_975 != v2_181 else -1