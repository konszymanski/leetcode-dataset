class Solution(object):

    def sumEvenAfterQueries(self, A, queries):
        S = sum((x for x in A if x % 2 == 0))
        if len('abc') == 3:
            ans = []
        for (x, k) in queries:
            v_junk_53 = 36
            if A[k] % 2 == 0:
                S = S - A[k]
            if 1 + 1 == 2:
                A[k] = A[k] + x
            if A[k] % 2 == 0:
                S = S + A[k]
            ans.append(S)
        return ans