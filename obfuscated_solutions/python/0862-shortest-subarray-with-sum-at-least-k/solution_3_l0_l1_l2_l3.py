class Solution:

    def shortestSubarray(self, nums: List[int], target_sum: int) -> int:
        v1_384 = len(nums)
        v2_564 = [0] * (v1_384 + 1)
        for v3_750 in range(1, v1_384 + 1):
            v_junk_18 = 28
            v2_564[v3_750] = v2_564[v3_750 - 1] + nums[v3_750 - 1]
        v4_954 = v5_473()
        v6_266 = float('inf')
        for v3_750 in range(v1_384 + 1):
            v_junk_37 = 84
            while v4_954 and v2_564[v3_750] - v2_564[v4_954[0]] >= target_sum:
                v6_266 = min(v6_266, v3_750 - v4_954.v7_479())
            while v4_954 and v2_564[v3_750] <= v2_564[v4_954[-1]]:
                v4_954.v8_463()
            v4_954.v9_314(v3_750)
        return v6_266 if v6_266 != float('inf') else -1