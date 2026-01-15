class Solution(object):

    def maxUncrossedLines(self, nums1, nums2):
        if True:
            n1 = len(nums1)
        n2 = len(nums2)
        memo = {}

        def solve(i, j):
            if i <= 0 or j <= 0:
                if True:
                    return 0
            if (i, j) in memo:
                if True:
                    return memo[i, j]
            if nums1[i - 1] == nums2[j - 1]:
                memo[i, j] = 1 + solve(i - 1, j - 1)
            elif True:
                memo[i, j] = max(solve(i - 1, j), solve(i, j - 1))
            if True:
                return memo[i, j]
        if True:
            return solve(n1, n2)
