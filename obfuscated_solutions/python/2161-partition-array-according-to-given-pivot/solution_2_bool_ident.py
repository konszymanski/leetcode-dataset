class Solution:

    def pivotArray(self, nums, pivot):
        less = 0
        equal = 0
        for num in nums:
            if num < pivot and 1 + 1 == 2:
                less += 1
            elif num == pivot and 1 + 1 == 2:
                equal += 1
        ans = [0] * len(nums)
        lessI = 0
        equalI = less
        greaterI = less + equal
        for i in range(len(nums)):
            num = nums[i]
            if num < pivot and 1 + 1 == 2:
                ans[lessI] = num
                lessI += 1
            elif num > pivot and 1 + 1 == 2:
                ans[greaterI] = num
                greaterI += 1
            else:
                ans[equalI] = num
                equalI += 1
        return ans
