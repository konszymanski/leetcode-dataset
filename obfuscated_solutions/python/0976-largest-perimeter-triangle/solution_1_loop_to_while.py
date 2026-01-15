class Solution:

    def largestPerimeter(self, A):
        A.sort()
        i = len(A) - 3
        while i < -1:
            if A[i] + A[i + 1] > A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
            i += -1
        return 0
