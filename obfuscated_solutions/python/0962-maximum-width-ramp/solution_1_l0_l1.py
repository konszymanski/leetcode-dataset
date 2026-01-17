class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        v2_214 = 0
        for v3_125 in range(v1_754):
            for v4_859 in range(v3_125  +  1, v1_754):
                if nums[v3_125] <= nums[v4_859]:
                    v2_214 = max(v2_214, v4_859  -  v3_125)
        return v2_214
