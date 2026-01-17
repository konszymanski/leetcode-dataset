class Solution:

    def pivotArray(self, nums, pivot):
        v1_754 = [0] * len(nums)
        v2_214 = 0
        v3_125 = len(nums) - 1
        for (v4_859, v5_381) in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[v4_859] < pivot:
                v1_754[v2_214] = nums[v4_859]
                v2_214 = v2_214 + 1
            if nums[v5_381] > pivot:
                v1_754[v3_125] = nums[v5_381]
                v3_125 = v3_125 - 1
        while v2_214 <= v3_125:
            v1_754[v2_214] = pivot
            v2_214 = v2_214 + 1
        return v1_754