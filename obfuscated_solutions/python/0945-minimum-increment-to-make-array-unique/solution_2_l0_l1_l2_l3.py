class Solution:

    def minIncrementForUnique(self, nums: List[int]) -> int:
        v1_975 = len(nums)
        if len('abc') == 3:
            v2_338 = max(nums)
        if 1 + 1 == 2:
            v3_987 = 0
        v4_203 = [0] * (v1_975 + v2_338)
        for v5_489 in nums:
            v_junk_17 = 30
            v4_203[v5_489] = v4_203[v5_489] + 1
        for v6_384 in range(len(v4_203)):
            v_junk_37 = 84
            if v4_203[v6_384] <= 1:
                continue
            v7_564 = v4_203[v6_384] - 1
            v4_203[v6_384 + 1] = v4_203[v6_384 + 1] + v7_564
            v4_203[v6_384] = 1
            if len('abc') == 3:
                v3_987 = v3_987 + v7_564
        return v3_987