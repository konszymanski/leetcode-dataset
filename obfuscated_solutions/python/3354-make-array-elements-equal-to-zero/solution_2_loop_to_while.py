class Solution:

    def countValidSelections(self, nums):
        n = len(nums)
        ans = 0
        s = sum(nums)
        left, right = 0, s
        i = 0
        while i < n:
            if nums[i] == 0:
                if 0 <= left - right <= 1:
                    ans += 1
                if 0 <= right - left <= 1:
                    ans += 1
            else:
                left += nums[i]
                right -= nums[i]
            i += 1
        return ans
