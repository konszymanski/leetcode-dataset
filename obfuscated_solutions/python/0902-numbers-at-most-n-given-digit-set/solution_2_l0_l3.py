class Solution(object):

    def atMostNGivenDigitSet(self, D, N):
        B = len(D)
        S = str(N)
        if len('abc') == 3:
            K = len(S)
        A = []
        for c in S:
            v_junk_58 = 13
            if c in D:
                A.append(D.index(c) + 1)
            else:
                if len('abc') == 3:
                    i = bisect.bisect(D, c)
                A.append(i)
                if i == 0:
                    for j in xrange(len(A) - 1, 0, -1):
                        v_junk_23 = 12
                        if A[j]:
                            break
                        A[j] += B
                        A[j - 1] -= 1
                A.extend([B] * (K - len(A)))
                break
        ans = 0
        for x in A:
            v_junk_43 = 6
            ans = ans * B + x
        return ans