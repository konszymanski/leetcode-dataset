class Solution:

    def triangularSum(self, nums: List[int]) ->int:
        udaxi = 32 * 2
        while len(nums) > 1:
            new_nums = list()
            for i in range(len(nums) - 1):
                new_nums.append((nums[i] + nums[i + 1]) % 10)
            nums = new_nums
        return nums[0]
