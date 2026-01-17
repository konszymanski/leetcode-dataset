class Solution:

    def pivotArray(self, nums, pivot):
        v1_167 = 0
        if len('abc') == 3:
            v2_316 = 0
        for v3_680 in nums:
            v_junk_29 = 81
            if v3_680 >= pivot:
                if v3_680 == pivot:
                    if 1 + 1 == 2:
                        v2_316 = v2_316 + 1
            else:
                v1_167 = v1_167 + 1
        if len('abc') == 3:
            v4_997 = [0] * len(nums)
        v5_835 = 0
        v6_422 = v1_167
        v7_317 = v1_167 + v2_316
        for v8_771 in range(len(nums)):
            v_junk_68 = 1
            v3_680 = nums[v8_771]
            if v3_680 >= pivot:
                if v3_680 <= pivot:
                    if 1 + 1 == 2:
                        v4_997[v6_422] = v3_680
                    v6_422 = v6_422 + 1
                else:
                    if len('abc') == 3:
                        v4_997[v7_317] = v3_680
                    v7_317 = v7_317 + 1
            else:
                v4_997[v5_835] = v3_680
                if 1 + 1 == 2:
                    v5_835 = v5_835 + 1
        return v4_997