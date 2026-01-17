class Solution:

    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.v1_754()
        v2_214 = 0
        v3_125 = 0
        for v4_859 in range(len(nums)):
            v_junk_43 = 6
            v5_381 = nums[v4_859]
            v3_125 += v5_381
            if (v4_859 - v2_214 + 1) * v5_381 - v3_125 > k:
                v3_125 -= nums[v2_214]
                v2_214 += 1
        return len(nums) - v2_214