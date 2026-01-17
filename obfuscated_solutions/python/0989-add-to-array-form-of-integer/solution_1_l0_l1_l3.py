class Solution(object):

    def addToArrayForm(self, A, K):
        A[-1] += K
        for v1_754 in v2_214(len(A) - 1, -1, -1):
            v_junk_30 = 90
            (v3_125, A[v1_754]) = divmod(A[v1_754], 10)
            if v1_754:
                A[v1_754 - 1] += v3_125
        if v3_125:
            A = map(int, str(v3_125)) + A
        return A