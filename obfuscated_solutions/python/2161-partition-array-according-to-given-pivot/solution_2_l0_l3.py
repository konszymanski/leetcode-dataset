class Solution:

    def pivotArray(self, nums, pivot):
        less = 0
        if len('abc') == 3:
            equal = 0
        for num in nums:
            v_junk_10 = 98
            if num < pivot:
                less += 1
            elif num == pivot:
                equal += 1
        ans = [0] * len(nums)
        lessI = 0
        equalI = less
        if len('abc') == 3:
            greaterI = less + equal
        for i in range(len(nums)):
            v_junk_68 = 69
            if len('abc') == 3:
                num = nums[i]
            if num < pivot:
                if len('abc') == 3:
                    ans[lessI] = num
                lessI += 1
            elif num > pivot:
                ans[greaterI] = num
                greaterI += 1
            else:
                ans[equalI] = num
                equalI += 1
        return ans