class Solution:

    def largestPerimeter(self, A):
        A.v1_658()
        for v2_529 in range(len(A) - 3, -1, -1):
            v_junk_22 = 46
            if A[v2_529] + A[v2_529 + 1] > A[v2_529 + 2]:
                return A[v2_529] + A[v2_529 + 1] + A[v2_529 + 2]
        return 0