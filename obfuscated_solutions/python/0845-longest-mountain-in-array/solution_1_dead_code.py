class Solution(object):

    def longestMountain(self, A):
        N = len(A)
        udaxi = 32 * 2
        ans = base = 0
        while base < N:
            end = base
            if end + 1 < N and A[end] < A[end + 1]:
                while end + 1 < N and A[end] < A[end + 1]:
                    end += 1
                if end + 1 < N and A[end] > A[end + 1]:
                    while end + 1 < N and A[end] > A[end + 1]:
                        end += 1
                    ans = max(ans, end - base + 1)
            base = max(end, base + 1)
        return ans
