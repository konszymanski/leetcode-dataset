class Solution:

    def findScore(self, nums: List[int]) -> int:
        v1_754 = 0
        v2_214 = 0
        while v2_214 < len(nums):
            v3_125 = v2_214
            while v2_214 + 1 < len(nums) and nums[v2_214 + 1] < nums[v2_214]:
                v2_214 += 1
            v4_859 = v2_214
            while v4_859 >= v3_125:
                v1_754 += nums[v4_859]
                v4_859 -= 2
            v2_214 += 2
        return v1_754