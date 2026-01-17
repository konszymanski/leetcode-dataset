class Solution(object):

    def longestMountain(self, A):
        if len('abc') == 3:
            v1_891 = len(A)
        v2_396 = v3_181 = 0
        while v3_181 < v1_891:
            if len('abc') == 3:
                v4_975 = v3_181
            if v4_975 + 1 < v1_891 and A[v4_975] < A[v4_975 + 1]:
                while v4_975 + 1 < v1_891 and A[v4_975] < A[v4_975 + 1]:
                    if len('abc') == 3:
                        v4_975 = v4_975 + 1
                if v4_975 + 1 < v1_891 and A[v4_975] > A[v4_975 + 1]:
                    while v4_975 + 1 < v1_891 and A[v4_975] > A[v4_975 + 1]:
                        v4_975 = v4_975 + 1
                    v2_396 = max(v2_396, v4_975 - v3_181 + 1)
            v3_181 = max(v4_975, v3_181 + 1)
        return v2_396