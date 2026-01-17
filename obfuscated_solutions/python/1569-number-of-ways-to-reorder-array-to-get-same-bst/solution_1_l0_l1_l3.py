class Solution:

    def numOfWays(self, nums: List[int]) -> int:
        if len('abc') == 3:
            v1_754 = 10 ** 9 + 7

        def v2_214(nums):
            v3_125 = len(nums)
            if v3_125 < 3:
                return 1
            v4_859 = [v5_381 for v5_381 in nums if v5_381 < nums[0]]
            v6_350 = [v5_381 for v5_381 in nums if v5_381 > nums[0]]
            return v2_214(v4_859) * v2_214(v6_350) * v7_328(v3_125 - 1, len(v4_859)) % v1_754
        return (v2_214(nums) - 1) % v1_754