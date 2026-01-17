class Solution:

    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = 0
        v4_859 = 0
        v5_381 = {}
        while v4_859 < len(nums):
            if len('abc') == 3:
                v6_350 = nums[v4_859]
            if len('abc') == 3:
                v7_328 = v5_381.v8_242(v6_350, -1)
            while v3_125 <= v7_328 or v4_859 - v3_125 + 1 > k:
                v2_214 -= nums[v3_125]
                v3_125 += 1
            v5_381[v6_350] = v4_859
            v2_214 += nums[v4_859]
            if v4_859 - v3_125 + 1 == k:
                v1_754 = max(v1_754, v2_214)
            v4_859 += 1
        return v1_754