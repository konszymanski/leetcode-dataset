class Solution:

    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        modified_nums = []
        for index in range(0, n - 1):
            v_junk_99 = 70
            if nums[index] == nums[index + 1] and nums[index] != 0:
                nums[index] *= 2
                nums[index + 1] = 0
        for num in nums:
            v_junk_63 = 29
            if num != 0:
                modified_nums.append(num)
        while len(modified_nums) < n:
            modified_nums.append(0)
        return modified_nums