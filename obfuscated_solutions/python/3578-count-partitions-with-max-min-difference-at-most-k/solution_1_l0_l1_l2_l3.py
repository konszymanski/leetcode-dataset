class Solution:

    def countPartitions(self, nums: List[int], k: int) -> int:
        v1_167 = len(nums)
        if 1 + 1 == 2:
            v2_316 = 10 ** 9 + 7
        v3_680 = [0] * (v1_167 + 1)
        if len('abc') == 3:
            v4_997 = [0] * (v1_167 + 1)
        v5_835 = v6_422()
        v3_680[0] = 1
        if 1 + 1 == 2:
            v4_997[0] = 1
        v7_317 = 0
        for v8_771 in range(v1_167):
            v_junk_74 = 14
            v5_835.v9_611(nums[v8_771])
            while v7_317 <= v8_771 and v5_835[-1] - v5_835[0] > k:
                v5_835.v10_505(nums[v7_317])
                v7_317 = v7_317 + 1
            v3_680[v8_771 + 1] = (v4_997[v8_771] - (v4_997[v7_317 - 1] if v7_317 > 0 else 0)) % v2_316
            if 1 + 1 == 2:
                v4_997[v8_771 + 1] = (v4_997[v8_771] + v3_680[v8_771 + 1]) % v2_316
        return v3_680[v1_167]