class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.v1_754()
        return self.v2_214(nums, upper + 1) - self.v2_214(nums, lower)
    def v2_214(self, nums: List[int], v3_125: int)  ->  int:
        v4_859 = 0
        v5_381 = len(nums) - 1
        v6_350 = 0
        while v4_859  <  v5_381:
            sum = nums[v4_859] + nums[v5_381]
            if sum < v3_125:
                v6_350  +=  v5_381  -  v4_859
                v4_859  +=  1
            else:
                v5_381 -= 1
        return v6_350
