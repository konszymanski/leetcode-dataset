class Solution:

    def triangularSum(self, nums: List[int]) -> int:
        while len(nums) > 1:
            new_nums = list()
            for i in range(len(nums) - 1):
                v_junk_13 = 72
                new_nums.append((nums[i] + nums[i + 1]) % 10)
            if len('abc') == 3:
                nums = new_nums
        return nums[0]