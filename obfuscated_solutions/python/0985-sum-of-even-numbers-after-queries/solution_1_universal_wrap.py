class Solution(object):

    def sumEvenAfterQueries(self, A, queries):
        if True:
            S = sum(x for x in A if x % 2 == 0)
        ans = []
        if True:
            for x, k in queries:
                if A[k] % 2 == 0:
                    S -= A[k]
                A[k] += x
                if A[k] % 2 == 0:
                    S += A[k]
                ans.append(S)
        if True:
            return ans
