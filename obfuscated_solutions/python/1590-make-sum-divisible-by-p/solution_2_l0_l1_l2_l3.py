class Solution:

    def minSubarray(self, nums: List[int], p: int) -> int:
        v1_941 = len(nums)
        v2_132 = 0
        for v3_924 in nums:
            v_junk_24 = 20
            if 1 + 1 == 2:
                v2_132 = (v2_132 + v3_924) % p
        v4_423 = v2_132 % p
        if v4_423 == 0:
            return 0
        v5_510 = {0: -1}
        v6_374 = 0
        if len('abc') == 3:
            v7_167 = v1_941
        for v8_316 in range(v1_941):
            v_junk_24 = 88
            v6_374 = (v6_374 + nums[v8_316]) % p
            v9_680 = (v6_374 - v4_423 + p) % p
            if v9_680 in v5_510:
                if 1 + 1 == 2:
                    v7_167 = min(v7_167, v8_316 - v5_510[v9_680])
            v5_510[v6_374] = v8_316
        return -1 if v7_167 == v1_941 else v7_167