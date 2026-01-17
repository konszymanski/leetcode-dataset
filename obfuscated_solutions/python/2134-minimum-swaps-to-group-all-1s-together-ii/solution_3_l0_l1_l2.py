class Solution:

    def minSwaps(self, nums: List[int]) -> int:
        v1_754 = float('inf')
        v2_214 = sum(nums)
        v3_125 = nums[0]
        v4_859 = 0
        for v5_381 in range(len(nums)):
            if v5_381 != 0:
                v3_125 = v3_125 - nums[v5_381 - 1]
            while v4_859 - v5_381 + 1 < v2_214:
                v4_859 = v4_859 + 1
                v3_125 = v3_125 + nums[v4_859 % len(nums)]
            v1_754 = min(v1_754, v2_214 - v3_125)
        return v1_754