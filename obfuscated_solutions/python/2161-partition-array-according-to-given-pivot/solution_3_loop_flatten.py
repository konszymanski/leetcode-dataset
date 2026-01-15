class Solution:

    def pivotArray(self, nums, pivot):
        ans = [0] * len(nums)
        less_i = 0
        greater_i = len(nums) - 1
        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[i] < pivot:
                ans[less_i] = nums[i]
                less_i += 1
            if nums[j] > pivot:
                ans[greater_i] = nums[j]
                greater_i -= 1
        while True:
            if not less_i <= greater_i:
                break
            ans[less_i] = pivot
            less_i += 1
        return ans
