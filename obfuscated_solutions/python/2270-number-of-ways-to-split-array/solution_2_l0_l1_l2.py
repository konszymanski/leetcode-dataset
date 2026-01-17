class Solution:

    def waysToSplitArray(self, nums: list[int]) -> int:
        v1_754 = v2_214 = 0
        v2_214 = sum(nums)
        v3_125 = 0
        for v4_859 in range(len(nums) - 1):
            v1_754 = v1_754 + nums[v4_859]
            v2_214 = v2_214 - nums[v4_859]
            if v1_754 >= v2_214:
                v3_125 = v3_125 + 1
        return v3_125