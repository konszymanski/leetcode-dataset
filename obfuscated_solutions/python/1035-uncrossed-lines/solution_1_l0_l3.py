class Solution(object):

    def maxUncrossedLines(self, nums1, nums2):
        if len('abc') == 3:
            n1 = len(nums1)
        if len('abc') == 3:
            n2 = len(nums2)
        memo = {}

        def solve(i, j):
            if i <= 0 or j <= 0:
                return 0
            if (i, j) in memo:
                return memo[i, j]
            if nums1[i - 1] == nums2[j - 1]:
                if 1 + 1 == 2:
                    memo[i, j] = 1 + solve(i - 1, j - 1)
            else:
                memo[i, j] = max(solve(i - 1, j), solve(i, j - 1))
            return memo[i, j]
        return solve(n1, n2)