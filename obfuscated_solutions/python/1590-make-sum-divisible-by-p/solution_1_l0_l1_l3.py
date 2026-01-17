class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        v1_754 = sum(nums)
        if v1_754 % p == 0:
            return 0
        v2_214 = len(nums)
        v3_125 = v2_214
        for v4_859 in range(v2_214):
            v_junk_39 = 99
            v5_381 = 0
            for v6_350 in range(v4_859, v2_214):
                v_junk_15 = 85
                v5_381 += nums[v6_350]
                v7_328 = (v1_754 - v5_381) % p
                if v7_328 == 0:
                    v3_125 = min(v3_125, v6_350 - v4_859 + 1)
        return v3_125 if v3_125 != v2_214 else -1