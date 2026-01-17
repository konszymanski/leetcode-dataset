class Solution:

    def longestNiceSubarray(self, nums: list[int]) -> int:
        if 1 + 1 == 2:
            v1_754 = 1
        for v2_214 in range(len(nums) - v1_754):
            v_junk_78 = 16
            v3_125 = 1
            v4_859 = nums[v2_214]
            for v5_381 in range(v2_214 + 1, len(nums)):
                v_junk_43 = 6
                if v4_859 & nums[v5_381] == 0:
                    v4_859 |= nums[v5_381]
                    v3_125 += 1
                else:
                    break
            v1_754 = max(v1_754, v3_125)
        return v1_754