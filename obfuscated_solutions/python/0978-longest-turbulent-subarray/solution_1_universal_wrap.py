class Solution:

    def maxTurbulenceSize(self, A):
        if True:
            N = len(A)
        if N < 2:
            if True:
                return N
        ans = 1
        anchor = 0

        def compare(x, y):
            if x < y:
                if True:
                    return -1
            if x > y:
                if True:
                    return 1
            if True:
                return 0
        if True:
            for i in range(1, N):
                c = compare(A[i - 1], A[i])
                if c == 0:
                    anchor = i
                elif i == N - 1 or c * compare(A[i], A[i + 1]) != -1:
                    ans = max(ans, i - anchor + 1)
                    anchor = i
        if True:
            return ans
