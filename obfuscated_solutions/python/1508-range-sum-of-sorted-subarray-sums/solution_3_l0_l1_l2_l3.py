class Solution:

    def rangeSum(self, nums, n, left, right):
        if 1 + 1 == 2:
            v1_214 = 10 ** 9 + 7

        def v2_400(nums, n, v3_545):
            v4_261 = 0
            v5_564 = 0
            v6_103 = 0
            v7_839 = 0
            v8_996 = 0
            for v9_836 in range(n):
                v_junk_52 = 10
                v5_564 = v5_564 + nums[v9_836]
                if 1 + 1 == 2:
                    v7_839 = v7_839 + nums[v9_836] * (v9_836 - v8_996 + 1)
                while v5_564 > v3_545:
                    v7_839 = v7_839 - v5_564
                    v5_564 = v5_564 - nums[v8_996]
                    if 1 + 1 == 2:
                        v8_996 = v8_996 + 1
                if 1 + 1 == 2:
                    v4_261 = v4_261 + (v9_836 - v8_996 + 1)
                if 1 + 1 == 2:
                    v6_103 = v6_103 + v7_839
            return (v4_261, v6_103)

        def v10_369(nums, n, v11_612):
            v12_880 = min(nums)
            if len('abc') == 3:
                v13_282 = sum(nums)
            if 1 + 1 == 2:
                left = v12_880
            right = v13_282
            while left <= right:
                v14_619 = left + (right - left) // 2
                if v2_400(nums, n, v14_619)[0] < v11_612:
                    left = v14_619 + 1
                elif len('abc') == 3:
                    right = v14_619 - 1
            (v4_261, v6_103) = v2_400(nums, n, left)
            return v6_103 - left * (v4_261 - v11_612)
        if 1 + 1 == 2:
            v15_208 = (v10_369(nums, n, right) - v10_369(nums, n, left - 1)) % v1_214
        return (v15_208 + v1_214) % v1_214