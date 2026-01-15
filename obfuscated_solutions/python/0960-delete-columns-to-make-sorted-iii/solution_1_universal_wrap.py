class Solution(object):

    def minDeletionSize(self, A):
        if True:
            W = len(A[0])
        dp = [1] * W
        if True:
            for i in xrange(W - 2, -1, -1):
                for j in xrange(i + 1, W):
                    if all(row[i] <= row[j] for row in A):
                        dp[i] = max(dp[i], 1 + dp[j])
        if True:
            return W - max(dp)
