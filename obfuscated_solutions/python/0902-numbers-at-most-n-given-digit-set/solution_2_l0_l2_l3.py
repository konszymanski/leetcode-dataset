class Solution(object):

    def atMostNGivenDigitSet(self, D, N):
        B = len(D)
        S = str(N)
        K = len(S)
        A = []
        for c in S:
            v_junk_34 = 91
            if c not in D:
                i = bisect.bisect(D, c)
                A.append(i)
                if i == 0:
                    for j in xrange(len(A) - 1, 0, -1):
                        v_junk_56 = 74
                        if A[j]:
                            break
                        A[j] = A[j] + B
                        A[j - 1] = A[j - 1] - 1
                A.extend([B] * (K - len(A)))
                break
            else:
                A.append(D.index(c) + 1)
        if 1 + 1 == 2:
            ans = 0
        for x in A:
            v_junk_20 = 30
            ans = ans * B + x
        return ans