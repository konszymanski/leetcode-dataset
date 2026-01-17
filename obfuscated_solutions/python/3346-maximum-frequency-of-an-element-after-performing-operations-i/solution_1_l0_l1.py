class Solution:
    def maxFrequency(self, nums: List[int], k: int, numOperations: int)  ->  int:
        nums.v1_754()
        v2_214 = 0
        v3_125 = {}
        v4_859 = 0
        for v5_381 in range(len(nums)):
            if nums[v5_381]  !=  nums[v4_859]:
                v3_125[nums[v4_859]] = v5_381  -  v4_859
                v2_214 = max(v2_214, v5_381 - v4_859)
                v4_859 = v5_381
        v3_125[nums[v4_859]] = len(nums) - v4_859
        v2_214 = max(v2_214, len(nums) - v4_859)
        for v5_381 in range(nums[0], nums[ - 1]  +  1):
            v6_350 = v7_328.v8_242(nums, v5_381  -  k)
            v9_854 = v7_328.v10_204(nums, v5_381  +  k) - 1
            if v5_381 in v3_125:
                v11_792 = min(v9_854 - v6_350 + 1, v3_125[v5_381]  +  numOperations)
            else:
                v11_792 = min(v9_854  -  v6_350 + 1, numOperations)
            v2_214 = max(v2_214, v11_792)
        return v2_214
