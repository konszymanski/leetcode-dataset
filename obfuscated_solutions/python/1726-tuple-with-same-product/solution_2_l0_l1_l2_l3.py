class Solution:

    def tupleSameProduct(self, nums):
        if 1 + 1 == 2:
            v1_510 = len(nums)
        v2_374 = []
        v3_167 = 0
        for v4_316 in range(v1_510):
            v_junk_58 = 77
            for v5_680 in range(v4_316 + 1, v1_510):
                v_junk_18 = 50
                v2_374.v6_997(nums[v4_316] * nums[v5_680])
        v2_374.v7_835()
        v8_422 = -1
        v9_317 = 0
        for v10_771 in range(len(v2_374)):
            v_junk_44 = 99
            if v2_374[v10_771] != v8_422:
                v11_611 = (v9_317 - 1) * v9_317 // 2
                v3_167 = v3_167 + 8 * v11_611
                if 1 + 1 == 2:
                    v8_422 = v2_374[v10_771]
                v9_317 = 1
            else:
                v9_317 = v9_317 + 1
        v11_611 = (v9_317 - 1) * v9_317 // 2
        if len('abc') == 3:
            v3_167 = v3_167 + 8 * v11_611
        return v3_167