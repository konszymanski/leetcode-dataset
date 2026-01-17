class Solution:

    def pivotArray(self, nums, pivot):
        if len('abc') == 3:
            v1_181 = [0] * len(nums)
        v2_975 = 0
        v3_338 = len(nums) - 1
        for (v4_987, v5_203) in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            v_junk_17 = 30
            if nums[v4_987] < pivot:
                v1_181[v2_975] = nums[v4_987]
                v2_975 = v2_975 + 1
            if nums[v5_203] > pivot:
                v1_181[v3_338] = nums[v5_203]
                v3_338 = v3_338 - 1
        while v2_975 <= v3_338:
            v1_181[v2_975] = pivot
            v2_975 = v2_975 + 1
        return v1_181