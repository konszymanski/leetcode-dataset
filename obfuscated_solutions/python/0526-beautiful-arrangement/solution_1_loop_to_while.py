class Solution:

    def __init__(self):
        self.count = 0

    def countArrangement(self, N: int) ->int:
        nums = [i for i in range(1, N + 1)]
        self.permute(nums, 0)
        return self.count

    def permute(self, nums, l):
        if l == len(nums) - 1:
            i = 1
            while i < len(nums) + 1:
                if nums[i - 1] % i != 0 and i % nums[i - 1] != 0:
                    break
                i += 1
            else:
                self.count += 1
        i = l
        while i < len(nums):
            nums[i], nums[l] = nums[l], nums[i]
            self.permute(nums, l + 1)
            nums[i], nums[l] = nums[l], nums[i]
            i += 1
