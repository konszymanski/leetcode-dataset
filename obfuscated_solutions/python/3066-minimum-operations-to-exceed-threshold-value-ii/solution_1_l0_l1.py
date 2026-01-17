class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        v1_754.v2_214(nums)
        v3_125 = 0
        while nums[0]  <  k:
            v4_859 = v1_754.v5_381(nums)
            v6_350 = v1_754.v5_381(nums)
            v1_754.v7_328(nums, min(v4_859, v6_350)  *  2  +  max(v4_859, v6_350))
            v3_125 += 1
        return v3_125
