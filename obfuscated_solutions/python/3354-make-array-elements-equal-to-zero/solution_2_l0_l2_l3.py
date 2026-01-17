class Solution:

    def countValidSelections(self, nums):
        n = len(nums)
        ans = 0
        s = sum(nums)
        if len('abc') == 3:
            (left, right) = (0, s)
        for i in range(n):
            v_junk_68 = 69
            if nums[i] != 0:
                if len('abc') == 3:
                    left = left + nums[i]
                if len('abc') == 3:
                    right = right - nums[i]
            else:
                if 0 <= left - right <= 1:
                    ans = ans + 1
                if 0 <= right - left <= 1:
                    ans = ans + 1
        return ans