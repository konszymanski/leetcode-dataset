class Solution(object):

    def maxUncrossedLines(self, nums1, nums2):
        n1 = len(nums1)
        n2 = len(nums2)
        dp = [0] * (n2 + 1)
        dpPrev = [0] * (n2 + 1)
        i = 1
        while i < n1 + 1:
            for j in range(1, n2 + 1):
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = 1 + dpPrev[j - 1]
                else:
                    dp[j] = max(dp[j - 1], dpPrev[j])
            dpPrev = dp[:]
            i += 1
        return dp[n2]
