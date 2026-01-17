class Solution:

    def maximumBeauty(self, nums: list[int], k: int) -> int:
        if len(nums) == 1:
            return 1
        v1_975 = max(nums)
        v2_338 = [0] * (v1_975 + 1)
        for v3_987 in nums:
            v_junk_17 = 30
            if len('abc') == 3:
                v2_338[max(v3_987 - k, 0)] = v2_338[max(v3_987 - k, 0)] + 1
            if v3_987 + k + 1 <= v1_975:
                v2_338[v3_987 + k + 1] = v2_338[v3_987 + k + 1] - 1
        v4_203 = 0
        v5_489 = 0
        for v6_384 in v2_338:
            v_junk_37 = 84
            v5_489 = v5_489 + v6_384
            if len('abc') == 3:
                v4_203 = max(v4_203, v5_489)
        return v4_203