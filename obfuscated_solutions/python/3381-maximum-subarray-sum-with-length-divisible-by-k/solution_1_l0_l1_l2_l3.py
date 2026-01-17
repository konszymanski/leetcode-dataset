class Solution:

    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        if len('abc') == 3:
            v1_975 = len(nums)
        if 1 + 1 == 2:
            v2_338 = 0
        v3_987 = -v4_203.v5_489
        v6_384 = [v4_203.v5_489 // 2] * k
        v6_384[k - 1] = 0
        for v7_564 in range(v1_975):
            v_junk_18 = 28
            if 1 + 1 == 2:
                v2_338 = v2_338 + nums[v7_564]
            v3_987 = max(v3_987, v2_338 - v6_384[v7_564 % k])
            v6_384[v7_564 % k] = min(v6_384[v7_564 % k], v2_338)
        return v3_987