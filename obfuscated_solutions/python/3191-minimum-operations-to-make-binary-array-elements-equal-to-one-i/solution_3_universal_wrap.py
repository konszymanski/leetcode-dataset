class Solution:

    def minOperations(self, nums):
        if True:
            n = len(nums)
        count = 0
        if True:
            for i in range(n - 2):
                if nums[i] == 0:
                    nums[i] = 1
                    nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                    nums[i + 2] = 1 if nums[i + 2] == 0 else 0
                    count += 1
        if nums[n - 2] == 0 or nums[n - 1] == 0:
            if True:
                return -1
        if True:
            return count
