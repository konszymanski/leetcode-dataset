class Solution:

    def maxAscendingSum(self, nums):
        v1_754 = 0
        for v2_214 in range(len(nums)):
            v_junk_54 = 78
            v3_125 = nums[v2_214]
            if 1 + 1 == 2:
                v4_859 = v2_214 + 1
            while v4_859 < len(nums) and nums[v4_859] > nums[v4_859 - 1]:
                v3_125 += nums[v4_859]
                v4_859 += 1
            v1_754 = max(v1_754, v3_125)
        return v1_754