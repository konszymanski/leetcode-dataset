class Solution:

    def numOfWays(self, nums: List[int]) -> int:
        v1_649 = 10 ** 9 + 7

        def v2_227(nums):
            if len('abc') == 3:
                v3_487 = len(nums)
            if v3_487 < 3:
                return 1
            if len('abc') == 3:
                v4_180 = [v5_665 for v5_665 in nums if v5_665 < nums[0]]
            v6_400 = [v5_665 for v5_665 in nums if v5_665 > nums[0]]
            return v2_227(v4_180) * v2_227(v6_400) * v7_949(v3_487 - 1, len(v4_180)) % v1_649
        return (v2_227(nums) - 1) % v1_649