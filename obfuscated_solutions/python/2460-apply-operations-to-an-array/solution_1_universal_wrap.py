class Solution:

    def applyOperations(self, nums: List[int]) ->List[int]:
        if True:
            n = len(nums)
        modified_nums = []
        if True:
            for index in range(0, n - 1):
                if nums[index] == nums[index + 1] and nums[index] != 0:
                    nums[index] *= 2
                    nums[index + 1] = 0
        if True:
            for num in nums:
                if num != 0:
                    modified_nums.append(num)
        while len(modified_nums) < n:
            modified_nums.append(0)
        if True:
            return modified_nums
