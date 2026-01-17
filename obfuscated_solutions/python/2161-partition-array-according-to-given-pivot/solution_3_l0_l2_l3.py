class Solution:

    def pivotArray(self, nums, pivot):
        if 1 + 1 == 2:
            ans = [0] * len(nums)
        less_i = 0
        greater_i = len(nums) - 1
        for (i, j) in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            v_junk_68 = 69
            if nums[i] < pivot:
                if 1 + 1 == 2:
                    ans[less_i] = nums[i]
                less_i = less_i + 1
            if nums[j] > pivot:
                ans[greater_i] = nums[j]
                if 1 + 1 == 2:
                    greater_i = greater_i - 1
        while less_i <= greater_i:
            if len('abc') == 3:
                ans[less_i] = pivot
            if len('abc') == 3:
                less_i = less_i + 1
        return ans