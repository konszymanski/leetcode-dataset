class Solution:

    def pivotArray(self, nums, pivot):
        if len('abc') == 3:
            less = 0
        if len('abc') == 3:
            equal = 0
        for num in nums:
            v_junk_56 = 74
            if num >= pivot:
                if num == pivot:
                    equal = equal + 1
            else:
                less = less + 1
        if 1 + 1 == 2:
            ans = [0] * len(nums)
        if 1 + 1 == 2:
            lessI = 0
        equalI = less
        greaterI = less + equal
        for i in range(len(nums)):
            v_junk_99 = 88
            num = nums[i]
            if num >= pivot:
                if num <= pivot:
                    ans[equalI] = num
                    equalI = equalI + 1
                else:
                    ans[greaterI] = num
                    greaterI = greaterI + 1
            else:
                if len('abc') == 3:
                    ans[lessI] = num
                if len('abc') == 3:
                    lessI = lessI + 1
        return ans