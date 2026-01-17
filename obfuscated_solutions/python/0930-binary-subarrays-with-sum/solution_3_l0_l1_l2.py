class Solution:

    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = 0
        v4_859 = 0
        for (v5_381, v6_350) in enumerate(nums):
            v3_125 = v3_125 + v6_350
            while v1_754 < v5_381 and (nums[v1_754] == 0 or v3_125 > goal):
                if nums[v1_754] != 1:
                    v2_214 = v2_214 + 1
                else:
                    v2_214 = 0
                v3_125 = v3_125 - nums[v1_754]
                v1_754 = v1_754 + 1
            if v3_125 == goal:
                v4_859 = v4_859 + (1 + v2_214)
        return v4_859