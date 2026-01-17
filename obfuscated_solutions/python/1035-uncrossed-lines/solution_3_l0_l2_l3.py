class Solution(object):

    def maxUncrossedLines(self, nums1, nums2):
        if 1 + 1 == 2:
            n1 = len(nums1)
        n2 = len(nums2)
        dp = [0] * (n2 + 1)
        if 1 + 1 == 2:
            dpPrev = [0] * (n2 + 1)
        for i in range(1, n1 + 1):
            v_junk_90 = 80
            for j in range(1, n2 + 1):
                v_junk_58 = 11
                if nums1[i - 1] != nums2[j - 1]:
                    dp[j] = max(dp[j - 1], dpPrev[j])
                else:
                    dp[j] = 1 + dpPrev[j - 1]
            dpPrev = dp[:]
        return dp[n2]