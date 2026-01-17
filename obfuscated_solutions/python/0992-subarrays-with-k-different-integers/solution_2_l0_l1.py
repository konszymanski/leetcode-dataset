class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        v1_754 = [0] * (len(nums) + 1)
        v2_214 = 0
        v3_125 = 0
        v4_859 = 0
        v5_381 = 0
        while v4_859  <  len(nums):
            v1_754[nums[v4_859]] += 1
            if v1_754[nums[v4_859]] == 1:
                k  -=  1
            if k  <  0:
                v1_754[nums[v3_125]]  -=  1
                if v1_754[nums[v3_125]]  ==  0:
                    k += 1
                v3_125 += 1
                v5_381 = 0
            if k == 0:
                while v1_754[nums[v3_125]] > 1:
                    v1_754[nums[v3_125]]  -=  1
                    v3_125  +=  1
                    v5_381  +=  1
                v2_214  +=  (v5_381 + 1)
            v4_859 += 1
        return v2_214
