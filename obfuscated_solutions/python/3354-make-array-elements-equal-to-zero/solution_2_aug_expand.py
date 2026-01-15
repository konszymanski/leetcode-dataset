class Solution:

    def countValidSelections(self, nums):
        n = len(nums)
        ans = 0
        s = sum(nums)
        left, right = 0, s
        for i in range(n):
            if nums[i] == 0:
                if 0 <= left - right <= 1:
                    ans = ans + 1
                if 0 <= right - left <= 1:
                    ans = ans + 1
            else:
                left = left + nums[i]
                right = right - nums[i]
        return ans
