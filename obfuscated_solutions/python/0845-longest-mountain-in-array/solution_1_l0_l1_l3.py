class Solution(object):

    def longestMountain(self, A):
        v1_754 = len(A)
        v2_214 = v3_125 = 0
        while v3_125 < v1_754:
            v4_859 = v3_125
            if v4_859 + 1 < v1_754 and A[v4_859] < A[v4_859 + 1]:
                while v4_859 + 1 < v1_754 and A[v4_859] < A[v4_859 + 1]:
                    v4_859 += 1
                if v4_859 + 1 < v1_754 and A[v4_859] > A[v4_859 + 1]:
                    while v4_859 + 1 < v1_754 and A[v4_859] > A[v4_859 + 1]:
                        v4_859 += 1
                    v2_214 = max(v2_214, v4_859 - v3_125 + 1)
            if 1 + 1 == 2:
                v3_125 = max(v4_859, v3_125 + 1)
        return v2_214