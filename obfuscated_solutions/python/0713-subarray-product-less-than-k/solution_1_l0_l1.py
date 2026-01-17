class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        v1_754 = 0
        v2_214 = 1
        v3_125 = 0
        for v4_859, v5_381 in enumerate(nums):
            v2_214 *= v5_381
            while v2_214  >=  k:
                v2_214  //=  nums[v3_125]
                v3_125  +=  1
            v1_754 += v4_859 - v3_125 + 1
        return v1_754
