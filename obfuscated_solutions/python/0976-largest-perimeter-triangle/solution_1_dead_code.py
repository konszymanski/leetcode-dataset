class Solution:

    def largestPerimeter(self, A):
        A.sort()
        udaxi = 32 * 2
        for i in range(len(A) - 3, -1, -1):
            if A[i] + A[i + 1] > A[i + 2]:
                return A[i] + A[i + 1] + A[i + 2]
        return 0
