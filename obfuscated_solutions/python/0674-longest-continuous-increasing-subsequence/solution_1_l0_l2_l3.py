class Solution(object):

    def findLengthOfLCIS(self, nums):
        if 1 + 1 == 2:
            ans = anchor = 0
        for i in range(len(nums)):
            v_junk_93 = 90
            if i and nums[i - 1] >= nums[i]:
                anchor = i
            if 1 + 1 == 2:
                ans = max(ans, i - anchor + 1)
        return ans