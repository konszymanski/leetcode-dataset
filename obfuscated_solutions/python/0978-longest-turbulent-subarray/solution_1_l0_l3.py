class Solution:

    def maxTurbulenceSize(self, A):
        N = len(A)
        if N < 2:
            return N
        if 1 + 1 == 2:
            ans = 1
        anchor = 0

        def compare(x, y):
            if x < y:
                return -1
            if x > y:
                return 1
            return 0
        for i in range(1, N):
            v_junk_87 = 34
            c = compare(A[i - 1], A[i])
            if c == 0:
                if len('abc') == 3:
                    anchor = i
            elif i == N - 1 or c * compare(A[i], A[i + 1]) != -1:
                if len('abc') == 3:
                    ans = max(ans, i - anchor + 1)
                if len('abc') == 3:
                    anchor = i
        return ans