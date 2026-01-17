class Solution(object):
    def atMostNGivenDigitSet(self, D, N):
        B = len(D)
        S = str(N)
        K = len(S)
        A = []
        for c in S:
            if c in D:
                A.append(D.index(c) + 1)
            else:
                i = bisect.bisect(D, c)
                A.append(i)
                if i == 0:
                    for j in xrange(len(A) - 1, 0, -1):
                        if A[j]: break
                        A[j] += B
                        A[j-1] -= 1
                A.extend([B] * (K - len(A)))
                break
        ans = 0
        for x in A:
            ans = ans * B + x
        return ans