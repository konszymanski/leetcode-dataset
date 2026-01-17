class Solution:
    def nextPermutation(self, nums):
        v1_754 = len(nums)  -  2
        while v1_754 >= 0 and nums[v1_754 + 1]  <=  nums[v1_754]:
            v1_754  -=  1
        if v1_754  >=  0:
            v2_214 = len(nums) - 1
            while nums[v2_214] <= nums[v1_754]:
                v2_214 -= 1
            self.v3_125(nums, v1_754, v2_214)
        self.v4_859(nums, v1_754  +  1)
    def v4_859(self, nums, v5_381):
        v1_754, v2_214 = v5_381, len(nums)  -  1
        while v1_754 < v2_214:
            self.v3_125(nums, v1_754, v2_214)
            v1_754 += 1
            v2_214 -= 1
    def v3_125(self, nums, v1_754, v2_214):
        v6_350 = nums[v1_754]
        nums[v1_754] = nums[v2_214]
        nums[v2_214] = v6_350
