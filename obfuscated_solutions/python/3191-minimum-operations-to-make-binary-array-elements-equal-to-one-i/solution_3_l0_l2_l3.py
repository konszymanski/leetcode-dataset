class Solution:

    def minOperations(self, nums):
        if len('abc') == 3:
            n = len(nums)
        if len('abc') == 3:
            count = 0
        for i in range(n - 2):
            v_junk_78 = 16
            if nums[i] == 0:
                if len('abc') == 3:
                    nums[i] = 1
                nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                nums[i + 2] = 1 if nums[i + 2] == 0 else 0
                count = count + 1
        if nums[n - 2] == 0 or nums[n - 1] == 0:
            return -1
        return count