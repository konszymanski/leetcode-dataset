class Solution(object):

    def findLengthOfLCIS(self, nums):
        ans = anchor = 0
        i = 0
        while i < len(nums):
            if i and nums[i - 1] >= nums[i]:
                anchor = i
            ans = max(ans, i - anchor + 1)
            i += 1
        return ans
