class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        v2_214 = [None]  *  v1_754
        v2_214[v1_754 - 1] = nums[v1_754 - 1]
        for v3_125 in range(v1_754 - 2, -1,  - 1):
            v2_214[v3_125] = max(v2_214[v3_125 + 1], nums[v3_125])
        v4_859 = 0
        v5_381 = 0
        v6_350 = 0
        while v5_381 < v1_754:
            while v4_859  <  v5_381 and nums[v4_859]  >  v2_214[v5_381]:
                v4_859  +=  1
            v6_350 = max(v6_350, v5_381 - v4_859)
            v5_381  +=  1
        return v6_350
