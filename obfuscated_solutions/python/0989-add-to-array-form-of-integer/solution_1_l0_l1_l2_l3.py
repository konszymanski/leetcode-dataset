class Solution(object):

    def addToArrayForm(self, A, K):
        A[-1] = A[-1] + K
        for v1_384 in v2_259(len(A) - 1, -1, -1):
            v_junk_80 = 38
            (v3_320, A[v1_384]) = divmod(A[v1_384], 10)
            if v1_384:
                A[v1_384 - 1] = A[v1_384 - 1] + v3_320
        if v3_320:
            A = map(int, str(v3_320)) + A
        return A