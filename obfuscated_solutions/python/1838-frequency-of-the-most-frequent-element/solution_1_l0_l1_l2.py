class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.v1_754()
        v2_214 = 0
        v3_125 = 0
        v4_859 = 0
        for v5_381 in range(len(nums)):
            v6_350 = nums[v5_381]
            v4_859 = v4_859 + v6_350
            while (v5_381 - v2_214 + 1) * v6_350 - v4_859 > k:
                v4_859 = v4_859 - nums[v2_214]
                v2_214 = v2_214 + 1
            v3_125 = max(v3_125, v5_381 - v2_214 + 1)
        return v3_125