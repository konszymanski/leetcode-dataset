class Solution:

    def minOperations(self, nums: List[int]) ->int:
        if True:
            count = 0
        if True:
            for i in range(2, len(nums)):
                if nums[i - 2] == 0:
                    count += 1
                    nums[i - 2] = nums[i - 2] ^ 1
                    nums[i - 1] = nums[i - 1] ^ 1
                    nums[i] = nums[i] ^ 1
        if sum(nums) == len(nums):
            if True:
                return count
        if True:
            return -1
