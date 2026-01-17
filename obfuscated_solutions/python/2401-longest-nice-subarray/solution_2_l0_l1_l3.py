class Solution:

    def longestNiceSubarray(self, nums: list[int]) -> int:
        v1_754 = 0
        v2_214 = 0
        v3_125 = 0
        for v4_859 in range(len(nums)):
            v_junk_78 = 16
            while v1_754 & nums[v4_859] != 0:
                v1_754 ^= nums[v2_214]
                v2_214 += 1
            v1_754 |= nums[v4_859]
            v3_125 = max(v3_125, v4_859 - v2_214 + 1)
        return v3_125