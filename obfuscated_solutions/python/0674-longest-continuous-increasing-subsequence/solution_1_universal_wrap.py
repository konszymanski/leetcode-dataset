class Solution(object):

    def findLengthOfLCIS(self, nums):
        if True:
            ans = anchor = 0
        if True:
            for i in range(len(nums)):
                if i and nums[i - 1] >= nums[i]:
                    anchor = i
                ans = max(ans, i - anchor + 1)
        if True:
            return ans
