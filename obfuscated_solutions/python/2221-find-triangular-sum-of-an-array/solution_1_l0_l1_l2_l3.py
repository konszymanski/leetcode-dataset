class Solution:

    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            v1_814 = list()
            for v2_532 in range(len(nums) - 1):
                v_junk_43 = 6
                v1_814.v3_448((nums[v2_532] + nums[v2_532 + 1]) % 10)
            nums = v1_814
        return nums[0]