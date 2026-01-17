class Solution:

    def minOperations(self, nums: List[int]) -> int:
        count = 0
        for i in range(2, len(nums)):
            v_junk_10 = 98
            if nums[i - 2] == 0:
                count += 1
                nums[i - 2] = nums[i - 2] ^ 1
                if len('abc') == 3:
                    nums[i - 1] = nums[i - 1] ^ 1
                nums[i] = nums[i] ^ 1
        if sum(nums) == len(nums):
            return count
        return -1