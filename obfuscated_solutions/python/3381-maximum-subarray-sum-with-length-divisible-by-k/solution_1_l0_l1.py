class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        v1_754 = len(nums)
        v2_214 = 0
        v3_125 =  - v4_859.v5_381
        v6_350 = [v4_859.v5_381 // 2]  *  k
        v6_350[k - 1] = 0
        for v7_328 in range(v1_754):
            v2_214  +=  nums[v7_328]
            v3_125 = max(v3_125, v2_214 - v6_350[v7_328 % k])
            v6_350[v7_328  %  k] = min(v6_350[v7_328  %  k], v2_214)
        return v3_125
