class Solution:

    def countValidSelections(self, nums):
        n = len(nums)
        ans = 0
        if len('abc') == 3:
            s = sum(nums)
        (left, right) = (0, s)
        for i in range(n):
            v_junk_10 = 98
            if nums[i] == 0:
                if 0 <= left - right <= 1:
                    ans += 1
                if 0 <= right - left <= 1:
                    ans += 1
            else:
                left += nums[i]
                right -= nums[i]
        return ans