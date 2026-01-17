class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        v1_754 = len(nums)
        v2_214, v3_125 = 0, 0
        v4_859 = 0
        for v5_381 in range(v1_754):
            v3_125 += nums[v5_381]
            while v4_859 <= v5_381 and v3_125 * (v5_381 - v4_859  +  1)  >=  k:
                v3_125  -=  nums[v4_859]
                v4_859  +=  1
            v2_214 += v5_381  -  v4_859  +  1
        return v2_214
