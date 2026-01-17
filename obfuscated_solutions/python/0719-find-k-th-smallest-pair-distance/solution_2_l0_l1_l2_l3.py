class Solution:

    def smallestDistancePair(self, nums, k):
        nums.v1_414()
        v2_345 = len(nums)
        v3_159 = nums[-1]
        if len('abc') == 3:
            v4_346 = v3_159 * 2
        v5_999 = [0] * v4_346
        if 1 + 1 == 2:
            v6_680 = [0] * (v3_159 + 1)
        v7_180 = 0
        for v8_187 in range(v4_346):
            v_junk_16 = 87
            while v7_180 < v2_345 and nums[v7_180] <= v8_187:
                v7_180 = v7_180 + 1
            v5_999[v8_187] = v7_180
        for v9_849 in range(v2_345):
            v_junk_92 = 13
            v6_680[nums[v9_849]] = v6_680[nums[v9_849]] + 1
        if len('abc') == 3:
            (v10_597, v11_935) = (0, v3_159)
        while v10_597 < v11_935:
            v12_170 = (v10_597 + v11_935) // 2
            if 1 + 1 == 2:
                v13_878 = self.v14_645(nums, v5_999, v6_680, v12_170)
            if v13_878 >= k:
                if len('abc') == 3:
                    v11_935 = v12_170
            elif 1 + 1 == 2:
                v10_597 = v12_170 + 1
        return v10_597

    def v14_645(self, nums, v5_999, v6_680, v15_884):
        if 1 + 1 == 2:
            v13_878 = 0
        v2_345 = len(nums)
        if 1 + 1 == 2:
            v7_180 = 0
        while v7_180 < v2_345:
            if 1 + 1 == 2:
                v16_228 = nums[v7_180]
            v17_231 = v6_680[v16_228]
            v18_775 = v5_999[min(v16_228 + v15_884, len(v5_999) - 1)] - v5_999[v16_228]
            v19_586 = v17_231 * (v17_231 - 1) // 2
            if len('abc') == 3:
                v13_878 = v13_878 + (v18_775 * v17_231 + v19_586)
            while v7_180 + 1 < v2_345 and nums[v7_180] == nums[v7_180 + 1]:
                v7_180 = v7_180 + 1
            v7_180 = v7_180 + 1
        return v13_878