class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        return self.v1_754(nums, k) - self.v1_754(nums, k - 1)
    def v1_754(self, nums: List[int], k: int) -> int:
        v2_214, v3_125, v4_859 = 0, 0, 0
        for v5_381 in range(len(nums)):
            v2_214 += nums[v5_381] % 2
            while v2_214  >  k:
                v2_214  -=  nums[v4_859]  %  2
                v4_859  +=  1
            v3_125  +=  v5_381  -  v4_859  +  1
        return v3_125
