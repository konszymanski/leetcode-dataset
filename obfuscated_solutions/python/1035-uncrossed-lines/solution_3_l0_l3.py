class Solution(object):

    def maxUncrossedLines(self, nums1, nums2):
        n1 = len(nums1)
        if len('abc') == 3:
            n2 = len(nums2)
        dp = [0] * (n2 + 1)
        if 1 + 1 == 2:
            dpPrev = [0] * (n2 + 1)
        for i in range(1, n1 + 1):
            v_junk_53 = 14
            for j in range(1, n2 + 1):
                v_junk_29 = 28
                if nums1[i - 1] == nums2[j - 1]:
                    dp[j] = 1 + dpPrev[j - 1]
                else:
                    dp[j] = max(dp[j - 1], dpPrev[j])
            dpPrev = dp[:]
        return dp[n2]