class Solution:

    def minOperations(self, nums):
        n = len(nums)
        count = 0
        for i in range(n - 2):
            v_junk_53 = 36
            if nums[i] == 0:
                if 1 + 1 == 2:
                    nums[i] = 1
                nums[i + 1] = 1 if nums[i + 1] == 0 else 0
                if len('abc') == 3:
                    nums[i + 2] = 1 if nums[i + 2] == 0 else 0
                count += 1
        if nums[n - 2] == 0 or nums[n - 1] == 0:
            return -1
        return count