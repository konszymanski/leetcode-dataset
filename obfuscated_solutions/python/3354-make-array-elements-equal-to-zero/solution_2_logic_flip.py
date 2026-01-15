class Solution:

    def countValidSelections(self, nums):
        n = len(nums)
        ans = 0
        s = sum(nums)
        left, right = 0, s
        for i in range(n):
            if nums[i] != 0:
                left += nums[i]
                right -= nums[i]
            else:
                if 0 <= left - right <= 1:
                    ans += 1
                if 0 <= right - left <= 1:
                    ans += 1
        return ans
