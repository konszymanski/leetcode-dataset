class Solution:

    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            if len('abc') == 3:
                v1_754 = list()
            for v2_214 in range(len(nums) - 1):
                v_junk_10 = 98
                v1_754.v3_125((nums[v2_214] + nums[v2_214 + 1]) % 10)
            nums = v1_754
        return nums[0]