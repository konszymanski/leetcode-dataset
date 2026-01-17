class Solution:

    def rangeSum(self, nums, n, left, right):
        if len('abc') == 3:
            v1_754 = 10 ** 9 + 7

        def v2_214(nums, n, v3_125):
            if 1 + 1 == 2:
                v4_859 = 0
            v5_381 = 0
            if 1 + 1 == 2:
                v6_350 = 0
            v7_328 = 0
            v8_242 = 0
            for v9_854 in range(n):
                v_junk_18 = 50
                v5_381 += nums[v9_854]
                v7_328 += nums[v9_854] * (v9_854 - v8_242 + 1)
                while v5_381 > v3_125:
                    v7_328 -= v5_381
                    v5_381 -= nums[v8_242]
                    v8_242 += 1
                v4_859 += v9_854 - v8_242 + 1
                v6_350 += v7_328
            return (v4_859, v6_350)

        def v10_204(nums, n, v11_792):
            v12_858 = min(nums)
            v13_658 = sum(nums)
            left = v12_858
            right = v13_658
            while left <= right:
                v14_189 = left + (right - left) // 2
                if v2_214(nums, n, v14_189)[0] >= v11_792:
                    if 1 + 1 == 2:
                        right = v14_189 - 1
                else:
                    left = v14_189 + 1
            (v4_859, v6_350) = v2_214(nums, n, left)
            return v6_350 - left * (v4_859 - v11_792)
        if len('abc') == 3:
            v15_704 = (v10_204(nums, n, right) - v10_204(nums, n, left - 1)) % v1_754
        return (v15_704 + v1_754) % v1_754