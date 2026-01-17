class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.v1_754(nums, k) - self.v1_754(nums, k  -  1)
    def v1_754(self, nums: List[int], v2_214: int) -> int:
        v3_125 = v4_859(int)
        v5_381 = 0
        v6_350  = 0
        for v7_328 in range(len(nums)):
            v3_125[nums[v7_328]]  +=  1
            while len(v3_125)  >  v2_214:
                v3_125[nums[v5_381]]  -=  1
                if v3_125[nums[v5_381]]  ==  0:
                    del v3_125[nums[v5_381]]
                v5_381 += 1
            v6_350  += v7_328  -  v5_381  +  1
        return v6_350
