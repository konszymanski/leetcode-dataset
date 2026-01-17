class Solution:
    def minDifference(self, nums: List[int]) -> int:
        v1_754 = len(nums)
        if v1_754 <= 4:
            return 0
        nums.v2_214()
        v3_125 = float("inf")
        for v4_859 in range(4):
            v5_381 = v1_754 - 4  +  v4_859
            v3_125 = min(v3_125, nums[v5_381]  -  nums[v4_859])
        return v3_125
