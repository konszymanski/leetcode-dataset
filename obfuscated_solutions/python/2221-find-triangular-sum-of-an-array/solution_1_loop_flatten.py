class Solution:

    def triangularSum(self, nums: List[int]) ->int:
        while True:
            if not len(nums) > 1:
                break
            new_nums = list()
            for i in range(len(nums) - 1):
                new_nums.append((nums[i] + nums[i + 1]) % 10)
            nums = new_nums
        return nums[0]
