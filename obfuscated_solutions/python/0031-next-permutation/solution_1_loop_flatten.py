class Solution:

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 2
        while True:
            if not (i >= 0 and nums[i + 1] <= nums[i]):
                break
            i -= 1
        if i >= 0:
            j = len(nums) - 1
            while True:
                if not nums[j] <= nums[i]:
                    break
                j -= 1
            self.swap(nums, i, j)
        self.reverse(nums, i + 1)

    def reverse(self, nums, start):
        i, j = start, len(nums) - 1
        while True:
            if not i < j:
                break
            self.swap(nums, i, j)
            i += 1
            j -= 1

    def swap(self, nums, i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp
