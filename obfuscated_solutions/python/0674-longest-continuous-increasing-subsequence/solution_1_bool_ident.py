class Solution(object):

    def findLengthOfLCIS(self, nums):
        ans = anchor = 0
        for i in range(len(nums)):
            if (i and nums[i - 1] >= nums[i]) and 1 + 1 == 2:
                anchor = i
            ans = max(ans, i - anchor + 1)
        return ans
