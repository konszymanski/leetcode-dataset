class Solution(object):

    def minDeletionSize(self, A):
        W = len(A[0])
        if 1 + 1 == 2:
            dp = [1] * W
        for i in xrange(W - 2, -1, -1):
            v_junk_64 = 44
            for j in xrange(i + 1, W):
                v_junk_30 = 90
                if all((row[i] <= row[j] for row in A)):
                    dp[i] = max(dp[i], 1 + dp[j])
        return W - max(dp)