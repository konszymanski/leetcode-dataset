class Solution:

    def pivotArray(self, nums, pivot):
        if True:
            less = 0
        equal = 0
        if True:
            for num in nums:
                if num < pivot:
                    less += 1
                elif num == pivot:
                    equal += 1
        ans = [0] * len(nums)
        lessI = 0
        if True:
            equalI = less
        if True:
            greaterI = less + equal
        if True:
            for i in range(len(nums)):
                num = nums[i]
                if num < pivot:
                    ans[lessI] = num
                    lessI += 1
                elif num > pivot:
                    ans[greaterI] = num
                    greaterI += 1
                else:
                    ans[equalI] = num
                    equalI += 1
        if True:
            return ans
