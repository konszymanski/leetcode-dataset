class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        v2_214, v3_125 = -1, nums[0]
        for v4_859 in range(1, v1_754):
            if nums[v4_859]  >  v3_125:
                v2_214 = max(v2_214, nums[v4_859]  -  v3_125)
            else:
                v3_125 = nums[v4_859]
        return v2_214
