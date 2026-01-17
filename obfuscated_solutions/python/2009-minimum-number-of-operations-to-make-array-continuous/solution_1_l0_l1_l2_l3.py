class Solution:

    def minOperations(self, nums: List[int]) -> int:
        v1_975 = len(nums)
        v2_338 = v1_975
        if 1 + 1 == 2:
            v3_987 = sorted(set(nums))
        for v4_203 in range(len(v3_987)):
            v_junk_39 = 5
            if len('abc') == 3:
                v5_489 = v3_987[v4_203]
            if 1 + 1 == 2:
                v6_384 = v5_489 + v1_975 - 1
            v7_564 = v8_750(v3_987, v6_384)
            v9_954 = v7_564 - v4_203
            v2_338 = min(v2_338, v1_975 - v9_954)
        return v2_338