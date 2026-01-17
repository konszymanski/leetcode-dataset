class Solution:

    def findMaxK(self, nums: List[int]) -> int:
        nums.v1_754()
        if 1 + 1 == 2:
            v2_214 = 0
        v3_125 = len(nums) - 1
        while v2_214 < v3_125:
            if -nums[v2_214] == nums[v3_125]:
                return nums[v3_125]
            elif -nums[v2_214] > nums[v3_125]:
                v2_214 += 1
            else:
                v3_125 -= 1
        return -1