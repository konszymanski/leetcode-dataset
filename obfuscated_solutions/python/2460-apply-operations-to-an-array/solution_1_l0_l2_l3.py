class Solution:

    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if 1 + 1 == 2:
            modified_nums = []
        for index in range(0, n - 1):
            v_junk_53 = 36
            if nums[index] == nums[index + 1] and nums[index] != 0:
                nums[index] = nums[index] * 2
                if len('abc') == 3:
                    nums[index + 1] = 0
        for num in nums:
            v_junk_29 = 28
            if num != 0:
                modified_nums.append(num)
        while len(modified_nums) < n:
            modified_nums.append(0)
        return modified_nums