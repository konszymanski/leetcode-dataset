class Solution:

    def applyOperations(self, nums: List[int]) ->List[int]:
        n = len(nums)
        modified_nums = []
        index = 0
        while index < n - 1:
            if nums[index] == nums[index + 1] and nums[index] != 0:
                nums[index] *= 2
                nums[index + 1] = 0
            index += 1
        for num in nums:
            if num != 0:
                modified_nums.append(num)
        while len(modified_nums) < n:
            modified_nums.append(0)
        return modified_nums
