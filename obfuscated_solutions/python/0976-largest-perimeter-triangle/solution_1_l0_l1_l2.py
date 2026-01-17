class Solution:

    def largestPerimeter(self, A):
        A.v1_754()
        for v2_214 in range(len(A) - 3, -1, -1):
            if A[v2_214] + A[v2_214 + 1] > A[v2_214 + 2]:
                return A[v2_214] + A[v2_214 + 1] + A[v2_214 + 2]
        return 0